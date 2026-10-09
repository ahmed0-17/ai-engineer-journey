from fastapi import FastAPI


app=FastAPI()

@app.get("/products")
def get_products(category:str):  #required query parameter
    return{
      "category":category

    }