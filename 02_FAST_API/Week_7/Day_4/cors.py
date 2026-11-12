from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI(title="test api",description="used for undersanding CORS concept")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/tasks/")
def products()->dict:
   return{
      "tasks":["Learning German","Learning FAST API"],
      "message":"User found."
   }
