from agents.planner import plan_migration
from agents.validator import validate_plan
from agents.executor import execute
from agents.reporter import generate_report

def run_pipeline(user_intent: str):
   plan = plan_migration(user_intent)
   validation = validate_plan(plan)
   if not validation["approved"]:
       return f"Blocked: {validation['reason']}"
   result = execute(plan)
   report = generate_report(result)
   return report