import requests
from app.memory import get_context, get_last_user_intent

def call_llm(prompt):
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma:2b",
                "prompt": prompt,
                "stream": False
            }
        )
        return res.json()["response"]
    except:
        return ""

def generate_response(user_text, data):

    # 🔥 MEMORY
    context = get_context()
    last_intent = get_last_user_intent()

    # 🔥 FOLLOW-UP DETECTION
    if "uska" in user_text.lower() or "uski" in user_text.lower():
        user_text = last_intent + " → " + user_text

    # ⚡ FAST RULE ENGINE
    if "sales" in user_text.lower():
        return f"Aaj ki sales ₹{data.get('sales')} hai"

    if "profit" in user_text.lower():
        return f"Aaj ka profit ₹{data.get('profit')} hai"

    if "stock" in user_text.lower():
        return f"Low stock: {', '.join(data.get('low_stock', []))}"

    if "expiry" in user_text.lower():
        return f"Expiry products: {', '.join(data.get('expiry', []))}"

    # 🤖 SMART AI (context-aware)
    prompt = f"""
    You are ShopSathi.

    Conversation:
    {context}

    User: {user_text}
    Data: {data}

    Answer in short Hindi (1 line).
    """

    response = call_llm(prompt)

    if not response:
        return "Mujhe samajh nahi aaya"

    return response.strip()