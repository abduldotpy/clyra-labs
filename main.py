import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import requests
parser = StrOutputParser()

load_dotenv()

model_text = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.0    
)
model_image = model_text = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-image" ,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.0    
)


prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert prompt rewriter for image generation.
      User will be input the prompt which could be needed some tweaking or no tweaking at all. You will be explaining the prompt further to enhance image generation
     just enhance the given prompt dont add add questions or extra things"""),
    ("human", "{user_input}"),
])

chain = prompt | model_text | parser | model_image

# nostreaming
response = chain.invoke({'What do you know about quatum computing'})
# print(response.content)

#streaming output
# for chunk in chain.stream({"user_input": "Generate Image of the red car"}):
#     print(chunk.content, end="", flush=True)


# # New line after streaming finishes
# print()


image_url = response.content # or similar extraction
image_data = requests.get(image_url).content
with open("generated_image.png", "wb") as f:
    f.write(image_data)
