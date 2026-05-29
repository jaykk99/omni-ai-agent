from fastapi import FastAPI
from pydantic import BaseModel
import os
from core.version_router import run_monico

app = FastAPI(title="Monico Agent")

class RunRequest(BaseModel):
    input: str
    user_id: str = "default"

@app.post("/run")
async def run_agent(request: RunRequest):
    result = await run_monico(request.input, request.user_id)
    return {"status": "success", "tier_used": os.getenv('MONICO_TIER', 'safe'), "result": result}

@app.get("/")
def root():
    return {"message": "Monico Agent Backend Ready - Set MONICO_TIER=paid for Uncensored mode"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
