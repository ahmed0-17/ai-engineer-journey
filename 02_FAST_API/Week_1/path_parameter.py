from fastapi import FastAPI



app=FastAPI()

@app.get("/products/{product_id}")
def get_product(product_id:int):
    return {
        "product_id":product_id,
        "message":"Product Found"
    }
