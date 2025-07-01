from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(temperature=0, model="gpt-4")

def analyze_pcf_file(file_text):
    messages = [
        SystemMessage(content="You are an expert in migrating apps from PCF to OpenShift."),
        HumanMessage(content=f"Analyze this file and suggest migration steps:\n{file_text}")
    ]
    return llm(messages).content
