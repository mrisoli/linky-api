"""
main API
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """
    GET /
    """
    return {"msg": "Hello World"}
