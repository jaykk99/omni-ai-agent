from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage
from litellm import completion
import subprocess
from typing import TypedDict, List
import os
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    messages: List
    next: str

# Tool: Run terminal commands (use with caution)
def run_terminal(cmd: str):
    try:
        result = subprocess.check_output(cmd, shell=True, text=True, timeout=30)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def call_llm(prompt: str, model: str = 'groq/llama3-1-70b-versatile'):
    response = completion(model=model, messages=[{'role': 'user', 'content': prompt}])
    return response.choices[0].message.content

# Basic agent workflow
print('Omni AI Agent initialized. Ready for commands.')
print('Paste your API keys in .env file.')

if __name__ == '__main__':
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            break
        response = call_llm(f'You are an autonomous agent. User said: {user_input}')
        print('Agent:', response)