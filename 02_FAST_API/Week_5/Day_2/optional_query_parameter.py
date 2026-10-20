from fastapi import FastAPI



app=FastAPI()

# @app.get("/products")
# def get_products(limit:int=10):  # optional query parameter
#     return {
#        "limit": limit
#     }


# # optional query parameter with None
# def get_products(category:str|None =None):
#     return {"Category":category}




#pratice
@app.get("/products")
def get_products(category:str|None=None,limit:int=10):
    return{
        "category":category,
        "Limit":limit
    }