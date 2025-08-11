import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = Groq(
    api_key=groq_api_key
    )

response = llm.chat.completions.create(
    messages= [
        {
        'role': 'system',
        'content': "what is python"
        }
        ],
    model = "llama3-70b-8192",
    temperature=1
)

print(response.choices[0].message.content)