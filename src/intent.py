def detect_intent(text):
    text = text.lower()

    if text.startswith(("hi", "hello", "hey")):
        return "greeting"

    if any(word in text for word in ["price", "plan", "cost", "refund", "refunds", "support"]):
        return "product_query"

    if any(p in text for p in ["i want", "i'd like", "sign me up", "i will try"]):
        return "high_intent"

    return "general"
