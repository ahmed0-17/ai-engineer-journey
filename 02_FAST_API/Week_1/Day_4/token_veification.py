from typing import Annotated
from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "my-secret-token":
        raise HTTPException(
            status_code=400,
            detail="Invalid token"
        )


@app.get(
    "/products/",
    dependencies=[Depends(verify_token)]
)
def get_products():
    return {"products": ["Mobile", "Laptop"]}