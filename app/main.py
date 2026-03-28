import asyncio
from app.intent import detect_intent
from app.api import fetch_data
from app.agent import generate_response
from app.voice.tts import speak_async

from app.memory import add_message
async def main():

    while True:
        user_text = input("You: ")
        add_message("user", user_text)

        data = fetch_data(user_text)

        response = generate_response(user_text, data)

        response = response.replace("\n", " ").strip()

        print("ShopSathi:", response)

        # 🔥 MEMORY SAVE
        add_message("user", user_text)
        add_message("bot", response)

        await speak_async(response)
if __name__ == "__main__":
    asyncio.run(main())