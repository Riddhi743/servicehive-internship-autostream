# ServiceHive Internship – AutoStream Conversational Agent

## Project Overview

This project is a conversational AI agent built for **AutoStream**, a fictional SaaS product that provides automated video editing tools for content creators.

The goal of the agent is to simulate how a real SaaS company can convert user conversations into qualified leads. Instead of acting like a simple chatbot, the agent is designed to understand user intent, answer product-related questions accurately using a local knowledge base, and safely trigger backend actions when a user shows high intent.

The agent can:

* Identify user intent (greeting, product inquiry, high intent)
* Answer pricing and policy questions using retrieval-based logic
* Maintain conversation state across multiple turns
* Collect user details and capture leads without triggering tools prematurely

---

## How to Run the Project Locally

### Prerequisites

* Python 3.9 or above

### Steps

```bash
pip install -r requirements.txt
python main.py
```

Once the program starts, interact with the agent through the terminal.

---

## Architecture & Design Explanation

The agent is built using a **state-driven conversational flow**, inspired by agent frameworks like LangGraph, but implemented manually to keep the logic transparent and easy to reason about.

Intent detection is handled using lightweight rule-based logic. This approach was chosen deliberately to ensure predictable behavior and to avoid hallucinations, especially for pricing and policy-related queries. User questions are answered using a **local JSON-based knowledge base**, which acts as a simple RAG (Retrieval-Augmented Generation) system. This guarantees that responses remain accurate and consistent with stored information.

Conversation memory is managed through a persistent state object that retains user details such as name, email, and creator platform across multiple turns. This state is reused throughout the conversation to ensure continuity and to safely control when backend actions are allowed.

The lead capture tool is explicitly gated using conversation state. The mock API function is triggered only after all required user details have been collected, ensuring that the tool is never executed prematurely. This design mirrors how real-world production systems safely handle user data and backend integrations.

Overall, the architecture prioritizes clarity, safety, and real-world applicability over over-engineering.

---

## WhatsApp Integration (Conceptual Explanation)

To integrate this agent with WhatsApp, the WhatsApp Business API can be used along with webhooks. Incoming WhatsApp messages would be sent to a backend service (for example, built using FastAPI).

Each incoming message would be forwarded to the conversational agent, which processes the message, updates the conversation state, and generates a response. The backend then sends the agent’s response back to the user via the WhatsApp API.

The same state-management and tool-gating logic used in this project can be extended to a production setup by storing conversation state in a database or cache (such as Redis), enabling scalable and reliable multi-user conversations.
