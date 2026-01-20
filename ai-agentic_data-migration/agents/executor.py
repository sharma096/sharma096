from MCP.mcp_bq_gcs_server import run_bq_to_gcs
# client = Client("bq-gcs-migration")

def execute(plan: dict):
   return run_bq_to_gcs(
       project="your-gcp-project",
       dataset="your_dataset",
       table="your_table",
       bucket="your-gcs-bucket"
   )