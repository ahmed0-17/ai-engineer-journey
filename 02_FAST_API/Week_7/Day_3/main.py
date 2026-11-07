
from datetime import timedelta
from typing import Annotated
import sys
from pathlib import Path

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

# Shared database path
DATABASE_PATH = (
    Path(__file__).resolve().parents[2]
    / "Week_6"
    / "Day_5"
)

sys.path.insert(0, str(DATABASE_PATH))

# Shared database and ORM model
from database import get_session
from models import User

from password_utils import verify_password
from token_utils import create_access_token, verify_access_token

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# 1. Authenticate user from PostgreSQL
def authenticate_user(
    session: Session,
    email: str,
    password: str
):
    statement = select(User).where(User.email == email)

    user = session.scalars(statement).first()

    if user is None:
        return None

    if not user.password_hash:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user


# 2. Login endpoint
@app.post("/login")
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(get_session)]
):
    user = authenticate_user(
        session,
        form_data.username,
        form_data.password
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=timedelta(minutes=30),
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


# 3. Get current user from JWT
def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[Session, Depends(get_session)]
):
    user_id = verify_access_token(token)

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        user_id = int(user_id)
    except (ValueError, TypeError):
        raise HTTPException(
            status_code=401,
            detail="Invalid token subject",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = session.get(User, user_id)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


# 4. Protected endpoint
@app.get("/users/me")
def read_current_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
    }
