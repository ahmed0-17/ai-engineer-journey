from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

# Temporary user for authorization practice
def get_current_user():
    return {
        "id": 1,
        "username": "ahmed",
        "role": "admin"
    }

# Check admin permission
def require_admin(
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user


@app.get("/profile")
def get_profile(
    user: dict = Depends(get_current_user)
):
    return {
        "message": "Profile accessed",
        "user": user
    }


@app.get("/admin")
def admin_dashboard(
    user: dict = Depends(require_admin)
):
    return {
        "message": "Welcome Admin",
        "user": user
    }


@app.get("/tasks")
def get_tasks(
    user: dict = Depends(get_current_user)
):
    return {
        "message": "Tasks accessed",
        "username": user["username"]
    }