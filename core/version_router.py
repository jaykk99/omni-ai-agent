# Monico Version Router (No Stripe)

import os
from typing import Dict, Any
from uncensored.orchestrator_uncensored import run_monico_uncensored
from safe.orchestrator_safe import run_monico_safe

TIER_CONFIG = {
    "free": "safe",
    "paid": "uncensored",
    "premium": "uncensored"
}

def get_user_tier(user_id: str) -> str:
    # Simple environment variable based (no Stripe keys needed)
    # Set MONICO_TIER=paid in your .env or Vercel dashboard
    return os.getenv("MONICO_TIER", "free").lower()

async def run_monico(user_input: str, user_id: str = "default", mission_id: str = None):
    tier = get_user_tier(user_id)
    version = TIER_CONFIG.get(tier, "safe")
    
    if version == "uncensored":
        print("🚀 Running Monico Uncensored (Paid Tier - HF Models)")
        return await run_monico_uncensored(user_input, mission_id)
    else:
        print("🛡️ Running Monico Safe (Sandbox)")
        return await run_monico_safe(user_input, mission_id)
