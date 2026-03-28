import edge_tts
import asyncio
from playsound import playsound
import time

async def speak_async(text):
    try:
        # 🔥 unique file name (fix permission issue)
        file = f"voice_{int(time.time())}.mp3"

        communicate = edge_tts.Communicate(
            text=text,
            voice="en-IN-PrabhatNeural"
        )

        await communicate.save(file)

        playsound(file)

    except Exception as e:
        print("Voice error:", e)