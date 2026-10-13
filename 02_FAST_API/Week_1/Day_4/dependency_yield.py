from fastapi import FastAPI,Depends
from typing import Annotated

app=FastAPI(title="My products API")


def get_resource():
    print("1. Resource setup")

    try:
        yield "My resources"

    finally:
        print("Resources cleanup")



@app.get("/test/")
def get_data(resource:Annotated[str,Depends(get_resource)]):
       return resource
