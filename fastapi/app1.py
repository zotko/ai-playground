from fastapi import FastAPI
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
import getpass
import os

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")

model = init_chat_model("gemini-2.5-flash-lite",
                        model_provider="google_genai",
                        max_tokens=50,
                        temperature=0.3
                        )

app = FastAPI()

@app.get("/")
def root_controller():
    return {"status": "healthy"}

@app.get("/chat")
def chat_controller(prompt: str = "Inspire me!"):
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=prompt)
    ]
    
    response = model.invoke(messages)
    
    statement = response.content
    return {"statement": statement}
