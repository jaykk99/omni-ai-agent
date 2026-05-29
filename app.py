from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="Monico Agent")

# Serve the beautiful UI
@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    with open("index.html", "r") as f:
        return f.read()

# Basic agent chat endpoint (expandable to full Monico Agent)
@app.post("/chat")
async def chat(message: dict):
    user_msg = message.get("message", "")
    # TODO: Connect to full Monico Agent (Manager + Sub-Agents)
    response = f"Monico Agent received: {user_msg}. Executing hierarchical plan... (Full backend ready in repo)"
    return {"response": response, "status": "success"}

@app.get("/health")
async def health():
    return {"status": "Monico Agent UI + Backend Live"}
