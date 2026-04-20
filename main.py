from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str

@app.post("/generate")
def post_generate(item: Item):
    item_data = item.model_dump()
    return item_data