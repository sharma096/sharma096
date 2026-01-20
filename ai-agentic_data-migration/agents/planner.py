from llm_client import call_llm
import json
def plan_migration(user_intent: str) -> dict:
   prompt = f"""
You are a data migration planner.
Convert this intent into a JSON plan.
Intent: {user_intent}
Return JSON with:
source_type, target_type, format, mode
"""
   response = call_llm(prompt)
   return json.loads(response)