import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
# Load API key from .env file
load_dotenv()
# 1. Setup the model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7,
    stream=True
)
# 2. Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{user_input}"),
])
# 3. Create the chain
chain = prompt | model
# 4. Run it
for chunk in chain.stream({"user_input": "Explain quantum computing in simple terms."}):
    print(chunk.content, end="", flush=True)

# New line after streaming finishes
print()