from src.intent import detect_intent
from src.knowledge import fetch_answer
from src.tools import mock_lead_capture
from src.state import ConversationState

state = ConversationState()

print("AutoStream Assistant is running...\n")

while True:
    user = input("You: ")
    intent = detect_intent(user)

    if intent == "greeting":
        print("Agent: Hey! Happy to help 🙂")

    elif intent == "product_query":
        print("Agent:", fetch_answer(user))

    elif intent == "high_intent":
        if not state.name:
            state.name = input("Agent: Before we proceed, may I know your name? ")

        if not state.email:
            state.email = input("Agent: Thanks! Could you share your email? ")

        if not state.platform:
            state.platform = input("Agent: Which platform do you mainly create content on? ")

        if state.is_complete():
            mock_lead_capture(state.name, state.email, state.platform)
            print("Agent: Awesome! Our team will get in touch soon.")
            break

    else:
        print("Agent: Got it. Tell me a bit more.")
