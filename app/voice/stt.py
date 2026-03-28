import asyncio
from app.intent import detect_intent
from app.api import fetch_data
from app.agent import generate_response
from app.voice.tts import speak

async def main():

    while True:
        user_text = input("You: ")

        intent = detect_intent(user_text)
        data = fetch_data(intent)

        response = generate_response(user_text, data)

        print("ShopSathi:", response)

        speak(response)

if __name__ == "__main__":
    asyncio.run(main())