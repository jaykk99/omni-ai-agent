from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Omni AI Agent Backend')

@app.get('/')
def root():
    return {'message': 'Omni AI Agent Cloud Backend Ready'}

# Add webhooks for Telegram/Slack later
