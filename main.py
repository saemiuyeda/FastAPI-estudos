from fastapi import FastAPI
from pydantic import BaseModel
import unicodedata

app = FastAPI()

class Item(BaseModel):
    text: str

def chatbot(message: str):
    processed_message = ""

    formatted_message = message.lower().strip()
    formatted_and_normalized_message = unicodedata.normalize('NFD', formatted_message)
    for char in formatted_and_normalized_message:
        if not unicodedata.combining(char):
            processed_message += char

    if processed_message == "ola":
        return "Olá! Como posso te ajudar?"
    else:
        return "Não entendi, poderia repetir?"

@app.post("/generate")
async def post_generate(item: Item):
    item_data = item.model_dump()
    return item_data