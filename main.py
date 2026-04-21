from fastapi import FastAPI
from pydantic import BaseModel
import unicodedata

app = FastAPI()

class Item(BaseModel):
    text: str

def normalize_text(message: str):
    processed_message = ""

    formatted_message = message.lower().strip()
    formatted_and_normalized_message = unicodedata.normalize('NFD', formatted_message)
    for char in formatted_and_normalized_message:
        if not unicodedata.combining(char):
            processed_message += char
    return processed_message

def generate_response(message: str):
    normalized_message = normalize_text(message)
    if normalized_message == "ola":
        return "Olá! Como posso ajudar?"
    else:
        return "Não entendi, poderia repetir?"

@app.post("/generate")
async def post_generate(item: Item):
    item_text = item.text

    chatbot = generate_response(item_text)

    return chatbot