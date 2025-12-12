import hashlib
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from passlib.context import CryptContext

# ----------------------
# Password hashing
# ----------------------

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _prehash_password(password: str) -> str:
    """
    Pre-hash password using SHA-256 to avoid bcrypt 72-byte limit
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def hash_password(password: str) -> str:
    prehashed = _prehash_password(password)
    return pwd_context.hash(prehashed)


def verify_password(password: str, hashed: str) -> bool:
    prehashed = _prehash_password(password)
    return pwd_context.verify(prehashed, hashed)


# ----------------------
# JWT configuration
# ----------------------

SECRET_KEY = "super-secret-key-change-this"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# ----------------------
# JWT validation (HTTP Bearer)
# ----------------------

security = HTTPBearer()


def get_current_admin(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        admin_email = payload.get("admin_email")
        organization = payload.get("organization")

        if not admin_email or not organization:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
            )

        return {
            "admin_email": admin_email,
            "organization": organization,
        }

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
