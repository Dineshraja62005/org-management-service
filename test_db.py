from app.database import org_collection

result = org_collection.insert_one({
    "organization_name": "demo_org",
    "admin_email": "demo@org.com"
})

print("Inserted ID:", result.inserted_id)
