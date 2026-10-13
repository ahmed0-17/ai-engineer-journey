from fastapi import FastAPI,status
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float
    stock: int


@app.post("/products",status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    return product