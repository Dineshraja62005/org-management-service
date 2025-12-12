from fastapi import APIRouter, HTTPException
from app.database import org_collection
from app.models.admin import AdminLoginRequest
from app.core.security import verify_password, create_access_token

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.post("/login")
def admin_login(data: AdminLoginRequest):
    # 1. Find admin by email
    admin = org_collection.find_one({"admin_email": data.email})

    if not admin:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # 2. Verify password
    if not verify_password(data.password, admin["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # 3. Create JWT token
    token = create_access_token({
        "admin_email": admin["admin_email"],
        "organization": admin["organization_name"]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
