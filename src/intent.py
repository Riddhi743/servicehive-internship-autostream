def detect_intent(text):
    text = text.lower()

    if text.startswith(("hi", "hello", "hey")):
        return "greeting"

    if "price" in text or "plan" in text or "cost" in text:
        return "product_query"

    if any(p in text for p in ["i want", "i'd like", "sign me up", "i will try"]):
        return "high_intent"

    return "general"
