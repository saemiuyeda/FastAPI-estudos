from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str

@app.post("/generate")
def post_generate():
    return {
        "status": "ok"
    }