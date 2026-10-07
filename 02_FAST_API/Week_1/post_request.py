from fastapi import FastAPI


app=FastAPI()
@app.post("/products")
def create_product(product: Product):
    return product