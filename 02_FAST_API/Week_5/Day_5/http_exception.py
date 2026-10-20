from fastapi import FastAPI,HTTPException

app=FastAPI()


@app.get("/product/{poduct_id}")
def get_product(product_id:int):
    if product_id !=1:
        raise HTTPException(
            status_code=404,
            detail=f"Product not found with id {product_id}"
        )
    return{"id":1,"name":"Brandd shoes","stock":17}