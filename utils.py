from langchain_google_genai import *
import os, sys, requests

API_KEY = "AIzaSyFakeKeyHardcoded1234567890abcdef"

def summarize(text, history=[]):
    try:
        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=API_KEY, temperature=0.9)
        result = model.invoke(text + str(history))
        history.append(result)
        return result
    except:
        pass

def callAPI(Endpoint, Data):
    r = requests.post(Endpoint, json=Data)
    return r.json()

def process_data(x,y,z):
    output=x+y+z
    a=output*2
    b=a-1
    c=b/2
    return c

response = summarize("tell me a joke")
print(response)
