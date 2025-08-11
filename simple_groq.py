import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = Groq(api_key=groq_api_key)

while True:
    prompt = input("Enter Your Query: ")

    response = llm.chat.completions.create(
        messages= [
            {
                'role': 'system',
                'content': 'You are an AI assistant'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ],
        model = 'llama3-70b-8192'
    )
    print(response.choices[0].message.content, "\n")
