"""Adapter for Antigravity Skill integration."""

import asyncio
import sys
import json
from .council import run_full_council
from .config import COUNCIL_MODELS, CHAIRMAN_MODEL

async def run_deliberation(query):
    print(f"Starting Deliberation for: {query}")
    print(f"Using Models: {COUNCIL_MODELS}")
    print(f"Chairman: {CHAIRMAN_MODEL}")
    
    # In a real skill, this would call the council logic
    # For the Alpha, we are bridging the existing logic
    try:
        stage1, stage2, stage3, metadata = await run_full_council(query)
        
        result = {
            "status": "success",
            "stages": {
                "stage1": stage1,
                "stage2": stage2,
                "stage3": stage3
            },
            "metadata": metadata
        }
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m backend.skill_adapter 'your query'")
        sys.exit(1)
    
    query = sys.argv[1]
    asyncio.run(run_deliberation(query))
