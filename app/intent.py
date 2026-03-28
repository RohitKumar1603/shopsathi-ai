def detect_intent(text):
    text = text.lower()

    if "sales" in text:
        return "GET_TODAY_SALES"

    elif "stock" in text:
        return "GET_LOW_STOCK"

    elif "expiry" in text:
        return "GET_EXPIRY"

    elif "profit" in text:
        return "GET_PROFIT"

    return "UNKNOWN"