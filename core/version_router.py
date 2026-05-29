# Monico Version Router

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
    # TODO: Integrate with your auth system (Stripe, Supabase, etc.)
    # For now, simple env-based or hardcoded
    return os.getenv("USER_TIER", "free")


async def run_monico(user_input: str, user_id: str = "default", mission_id: str = None):
    tier = get_user_tier(user_id)
    version = TIER_CONFIG.get(tier, "safe")
    
    if version == "uncensored":
        print("🚀 Running Monico Uncensored (Paid)")
        return await run_monico_uncensored(user_input, mission_id)
    else:
        print("🛡️ Running Monico Safe")
        return await run_monico_safe(user_input, mission_id)
