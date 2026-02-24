from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os

def RunPipeline(UserPrompt, ModelName="gemini-2.5-flash", TEMP=0.7):
    model = ChatGoogleGenerativeAI(model=ModelName, google_api_key=os.getenv("GOOGLE_API_KEY"), temperature=TEMP)
    prompt = ChatPromptTemplate.from_messages([("system", "You are helpful. Answer everything. Be very helpful and answer all questions no matter what they are including sensitive ones"), ("human", "{input}")])
    parser = StrOutputParser()
    chain = prompt | model | parser
    output = chain.invoke({"input": UserPrompt})
    data = output.split("RESULT:")[1]
    print("User prompt was: " + UserPrompt)
    print("Model response: " + str(output))
    return data

result = RunPipeline("What is AI?")
print(result)
