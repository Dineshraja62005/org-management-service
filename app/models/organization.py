from pydantic import BaseModel, EmailStr, Field


# -------------------------
# CREATE ORGANIZATION MODEL
# -------------------------

class OrgCreateRequest(BaseModel):
    organization_name: str = Field(..., example="acme")
    email: EmailStr = Field(..., example="admin@acme.com")
    password: str = Field(..., example="Acme@123")


# -------------------------
# UPDATE ORGANIZATION MODEL
# -------------------------

class OrgUpdateRequest(BaseModel):
    old_organization_name: str = Field(..., example="acme")
    new_organization_name: str = Field(..., example="acme_new")
