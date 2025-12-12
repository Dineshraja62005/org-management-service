from fastapi import APIRouter, HTTPException, Depends
from app.database import db, org_collection
from app.models.organization import OrgCreateRequest, OrgUpdateRequest
from app.core.security import hash_password, get_current_admin

router = APIRouter(
    prefix="/org",
    tags=["Organization"]
)

# -------------------------
# CREATE ORGANIZATION
# -------------------------

@router.post("/create")
def create_organization(data: OrgCreateRequest):
    # Check if org already exists
    if org_collection.find_one({"organization_name": data.organization_name}):
        raise HTTPException(status_code=400, detail="Organization already exists")

    collection_name = f"org_{data.organization_name}"

    org_collection.insert_one({
        "organization_name": data.organization_name,
        "collection_name": collection_name,
        "admin_email": data.email,
        "password_hash": hash_password(data.password)
    })

    # Create org-specific collection
    db.create_collection(collection_name)

    return {
        "message": "Organization created successfully",
        "organization": data.organization_name
    }


# -------------------------
# GET ORGANIZATION
# -------------------------

@router.get("/get")
def get_organization(organization_name: str):
    org = org_collection.find_one(
        {"organization_name": organization_name},
        {"_id": 0, "password_hash": 0}
    )

    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")

    return org


# -------------------------
# UPDATE ORGANIZATION
# -------------------------

@router.put("/update")
def update_organization(
    data: OrgUpdateRequest,
    current_admin: dict = Depends(get_current_admin)
):
    # Authorization check
    if current_admin["organization"] != data.old_organization_name:
        raise HTTPException(status_code=403, detail="Not authorized")

    org = org_collection.find_one(
        {"organization_name": data.old_organization_name}
    )
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")

    # New name already exists
    if org_collection.find_one(
        {"organization_name": data.new_organization_name}
    ):
        raise HTTPException(
            status_code=400,
            detail="New organization name already exists"
        )

    old_collection = org["collection_name"]
    new_collection = f"org_{data.new_organization_name}"

    # Copy data to new collection
    docs = list(db[old_collection].find())
    if docs:
        db[new_collection].insert_many(docs)

    # Drop old collection
    db.drop_collection(old_collection)

    # Update master record
    org_collection.update_one(
        {"organization_name": data.old_organization_name},
        {
            "$set": {
                "organization_name": data.new_organization_name,
                "collection_name": new_collection
            }
        }
    )

    return {"message": "Organization updated successfully"}


# -------------------------
# DELETE ORGANIZATION
# -------------------------

@router.delete("/delete")
def delete_organization(
    organization_name: str,
    current_admin: dict = Depends(get_current_admin)
):
    # Authorization check
    if current_admin["organization"] != organization_name:
        raise HTTPException(status_code=403, detail="Not authorized")

    org = org_collection.find_one({"organization_name": organization_name})
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")

    # Drop org collection
    db.drop_collection(org["collection_name"])

    # Remove from master DB
    org_collection.delete_one({"organization_name": organization_name})

    return {"message": "Organization deleted successfully"}
