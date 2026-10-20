from fastapi import FastAPI

app=FastAPI()

@app.get("/products")
def get_products(limit:int=10,category:str="all"):
    return{
        "Limit":limit,
        "category":category
    }