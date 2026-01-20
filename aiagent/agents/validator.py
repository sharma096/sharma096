from google.cloud import bigquery
from migrationai.state.agentstate import MigrationState

MAX_FULL_EXPORT_TB = 5

def validator_agent(state: MigrationState) -> MigrationState:
   client = bigquery.Client(project=state["project"])
   table_ref = f"{state['project']}.{state['dataset']}.{state['table']}"
   table = client.get_table(table_ref)

   size_tb = table.num_bytes / (1024**4)

   partitioned = table.time_partitioning is not None

   validation = {
      "size_tb": round(size_tb, 2),
      "partitioned": partitioned,
      "allowed": True,
      "warnings": [],
      "blocked": False
      }
   
   if state["plan"]["load_type"] == "full" and size_tb > MAX_FULL_EXPORT_TB:
      validation["allowed"] = False
      validation["blocked"] = True
      validation["warnings"].append("Full export > 5TB blocked by policy")


      if not partitioned:
         validation["warnings"].append("Source table is not partitioned")


         state["validation"] = validation
         state["logs"].append("Validator: Validation completed")


      if validation["blocked"]:
         state["status"] = "BLOCKED"


      return state


