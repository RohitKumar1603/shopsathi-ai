conversation = []

def add_message(role, content):
    conversation.append({
        "role": role,
        "content": content
    })

def get_context():
    # 🔥 last 5 messages
    return conversation[-5:]

def get_last_user_intent():
    for msg in reversed(conversation):
        if msg["role"] == "user":
            return msg["content"]
    return ""