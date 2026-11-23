# Import required module.
from fastapi import APIRouter

router = APIRouter(tags=["Basic Routes"])


# Root endpoint.
# Example: /
@router.get("/")
def greet():
    return {
        "message": "Hello I Am Sahil And Welcome to The FastAPI!!"
    }


# Greeting endpoint.
# Example: /Hello
@router.get("/Hello")
def Hello():
    return {"message": "Hello Sahil!!!"}