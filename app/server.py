from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import generate_response
from app.api import fetch_data
from app.memory import add_message

app = FastAPI()

class Query(BaseModel):
    text: str

@app.post("/chat")
async def chat(query: Query):

    user_text = query.text

    data = fetch_data(user_text)

    add_message("user", user_text)

    response = generate_response(user_text, data)

    add_message("bot", response)

    return {"response": response}