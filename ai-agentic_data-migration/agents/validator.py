from llm_client import call_llm
import json
def validate_plan(plan: dict) -> dict:
   prompt = f"""
Validate this data migration plan for risks.
Return JSON with:
approved (true/false), reason
Plan: {plan}
"""
   response = call_llm(prompt)
   return json.loads(response)