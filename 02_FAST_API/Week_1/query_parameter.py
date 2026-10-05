from fastapi import FastAPI



app=FastAPI()

# optional parameter
@app.get("/products")
def get_products(limit:int=10):
    return {
       "limit": limit
    }
