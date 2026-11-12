from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI(title="test api",description="used for undersanding CORS concept")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
     max_age=10,
)



# Security Headers Middleware
@app.middleware("http")
async def security_headers(request: Request, call_next):

    response = await call_next(request)

    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

    return response




@app.get("/tasks/")
def products()->dict:
   return{
      "tasks":["Learning German","Learning FAST API"],
      "message":"User found."
   }



@app.put("/tasks")
def update_task():
    return {
        "message": "Task updated successfully"
    }