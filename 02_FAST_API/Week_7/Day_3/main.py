import sys
from datetime import timedelta,datetime,timezone
from typing import Annotated
from pathlib import Path
from pydantic import BaseModel

from fastapi import FastAPI, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from password_utils import verify_password
from token_utils import create_access_token, verify_access_token,generate_refresh_token,hash_refresh_token

# Shared database path
DATABASE_PATH = (
    Path(__file__).resolve().parents[2]
    / "Week_6"
    / "Day_5"
)

sys.path.insert(0, str(DATABASE_PATH))

# Shared database and ORM model
from database import get_session,engine
from models import User,RefreshToken

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

class RefreshTokenRequest(BaseModel):
    refresh_token: str




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




def save_refresh_token(user_id: int):

    token, expires_at = generate_refresh_token()

    token_hash = hash_refresh_token(token)

    with Session(engine) as session:
        with session.begin():

            db_token = RefreshToken(
                user_id=user_id,
                token_hash=token_hash,
                expires_at=expires_at
            )

            session.add(db_token)

    return token



def validate_refresh_token(token: str):

    token_hash = hash_refresh_token(token)

    with Session(engine) as session:

        statement = select(RefreshToken).where(
            RefreshToken.token_hash == token_hash
        )

        db_token = session.scalar(statement)

        if db_token is None:
            return None

        if db_token.revoked:
            return None

        if db_token.expires_at <= datetime.now(timezone.utc):
            return None

        return db_token.user_id







def rotate_refresh_token(token: str):

    token_hash = hash_refresh_token(token)

    with Session(engine) as session:
        with session.begin():

            statement = select(RefreshToken).where(
                RefreshToken.token_hash == token_hash
            )

            db_token = session.scalar(statement)

            if db_token is None:
                return None

            if db_token.revoked:
                return None

            if db_token.expires_at <= datetime.now(timezone.utc):
                return None

            # Revoke old refresh token
            db_token.revoked = True

            # Generate new refresh token
            new_token, expires_at = generate_refresh_token()

            # Hash new token
            new_token_hash = hash_refresh_token(new_token)

            # Save new token hash
            new_db_token = RefreshToken(
                user_id=db_token.user_id,
                token_hash=new_token_hash,
                expires_at=expires_at
            )

            session.add(new_db_token)

        return new_token










@app.post("/refresh")
def refresh_access_token(data: RefreshTokenRequest):

    new_refresh_token = rotate_refresh_token(data.refresh_token)

    if new_refresh_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token"
        )

    new_access_token = create_access_token(
        data={"sub": str(validate_refresh_token(new_refresh_token))}
    )

    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer"
    }


#     # Generate initial token
# old_token = save_refresh_token(user_id=1)

# # Rotate token
# new_token = rotate_refresh_token(old_token)

# # Validate both tokens
# old_result = validate_refresh_token(old_token)
# new_result = validate_refresh_token(new_token)

# print("Old Token:", old_result)
# print("New Token:", new_result)


