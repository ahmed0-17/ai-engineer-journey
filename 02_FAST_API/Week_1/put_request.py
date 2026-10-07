from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float
    stock: int


@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    return {
        "product_id": product_id,
        "product": product
    }