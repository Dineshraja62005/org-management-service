from fastapi import FastAPI
from app.routes import org, auth

app = FastAPI(
    title="Organization Management Service",
    version="1.0.0",
    description="Multi-tenant backend with JWT authentication"
)

# Register routers
app.include_router(org.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Backend project started 🚀"}
