from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    stock: int | None = None


products = {
    10: {
        "name": "Electric kettle",
        "price": 2250,
        "stock": 12
    },
    11: {
        "name": "Laptop",
        "price": 150000,
       "stock": 5
    }
}


@app.patch("/products/{product_id}")
def update_product(product_id: int, product: ProductUpdate):

    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    update_data = product.model_dump(exclude_unset=True)

    products[product_id].update(update_data)

    return {
        "message": "Product updated successfully",
        "product": products[product_id]
    }