import openai
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY") 
llm = ChatGroq(api_key=groq_api_key, model_name="llama3-70b-8192")
prompt = PromptTemplate.from_template("What is LangChain")

chain = RunnableSequence(first = prompt, last = llm)

response = chain.invoke({})
print(response)

