import json

def load_kb():
    with open("data/autostream_kb.json") as f:
        return json.load(f)

def fetch_answer(question):
    kb = load_kb()
    q = question.lower()

    if "basic" in q:
        return kb["pricing"]["basic"]

    if "pro" in q:
        return kb["pricing"]["pro"]

    if "refund" in q:
        return kb["policies"]["refund"]

    if "support" in q:
        return kb["policies"]["support"]

    return "I'm not completely sure about that yet."
