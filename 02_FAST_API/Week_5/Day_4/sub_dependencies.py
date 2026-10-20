from typing import Annotated
from fastapi import FastAPI, Depends

app = FastAPI()


def get_token():
    return "user-token-123"


def get_current_user(
    token: Annotated[str, Depends(get_token)]
):
    return {
        "username": "Ahmed",
        "token": token
    }


@app.get("/profile/")
def get_profile(
    user: Annotated[dict, Depends(get_current_user)]
):
    return user