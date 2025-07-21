from fastapi import FastAPI
from typing import List

app = FastAPI()

# Sample in-memory data
items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"},
]

@app.get("/status")
def read_status():
    return {"status": "ok", "message": "Service is running"}

@app.get("/items")
def read_items() -> List[dict]:
    return items
