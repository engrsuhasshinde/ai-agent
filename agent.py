from openai import OpenAI
import os
import json
from datetime import datetime

SYSTEM_PROMPT = (
    "You are an expert coding assistant. "
    "Be concise and clear in your responses."
)
CHAT_DIR = "chat_history"

def create_chat_file():
    os.makedirs(CHAT_DIR, exist_ok = True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{CHAT_DIR}/chat_{timestamp}.json"

def save_conversation(filename, conversation):
    with open(filename, "w") as f:
        json.dump(conversation, f, indent = 4)

client = OpenAI(
    base_url = "http://localhost:11434/v1",
    api_key = "ollama"
)

chat_file = create_chat_file()

conversation = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

print("Suhas's Coding Assistant (🤖): Hello! (type 'exit' to quit)")
print("=" * 50)

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Suhas's Coding Assistant (🤖): Goodbye!")
        break

    conversation.append({ "role": "user", "content": user_input })

    try:
        response = client.chat.completions.create(
            model = 'phi4-mini',
            messages = conversation,
            stream = True  # Enable streaming responses
        )

        full_response = ""

        print("🤖: ", end = "", flush = True)

        # Stream output response
        for chunk in response:
            content = chunk.choices[0].delta.content or ""
            print(content, end = "", flush = True)  # Print the streamed content in real-time
            full_response += content

        print("\n")  # Print a newline after the full response is received

        conversation.append({ "role": "assistant", "content": full_response })  # Add the assistant's response to the conversation history
        
        save_conversation(chat_file, conversation)  # Save the conversation history to a file
    except Exception as e:
        print(f"Error: {e}")
        conversation.pop()  # Remove the last unanswered user message from history if there's an error