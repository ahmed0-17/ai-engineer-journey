import os
import jwt
import secrets
import hashlib
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")

REFRESH_TOKEN_EXPIRE_DAYS = int(
    os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7")
)

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY environment variable is missing")



def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + expires_delta

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt



def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:
            return None

        return user_id

    except jwt.InvalidTokenError:
        return None






def generate_refresh_token():

    refresh_token = secrets.token_urlsafe(64)

    expires_at = (
        datetime.now(timezone.utc)
        + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    )

    return refresh_token, expires_at    



def hash_refresh_token(token: str) -> str:

    token_bytes = token.encode("utf-8")

    token_hash = hashlib.sha256(token_bytes).hexdigest()

    return token_hash