import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = Groq(
    api_key=groq_api_key
)

# Memory: Store full conversation history
message_history = [
    {
        'role': 'system',
        'content': 'You are an AI assistant.'
    }
]

while True:
    prompt = input("You: ")
    if prompt.lower() in ['exit', 'quit']:
        print("Chat ended.")
        break

    # Add user message to memory
    message_history.append({
        'role': 'user',
        'content': prompt
    })

    # Get response from model
    response = llm.chat.completions.create(
        messages=message_history,
        model="llama3-70b-8192",
        temperature = 0.2
    )

    reply = response.choices[0].message.content

    # Add assistant response to memory
    message_history.append({
        'role': 'assistant',
        'content': reply
    })

    print("AI:", reply, "\n")
