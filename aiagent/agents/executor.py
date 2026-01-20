from mcp import ClientSession
import asyncio
from migrationai.state.agentstate import MigrationState

async def call_mcp_tool(project, dataset, table, bucket):
    async with ClientSession("http://localhost:3333") as session:
        result = await session.call_tool(
            "bq_to_gcs_parquet",
            {
            "project": project,
            "dataset": dataset,
            "table": table,
            "bucket": bucket
            }
            )
        return result

def executor_agent(state: dict):
    if state["status"] == "BLOCKED":
        return state


    result = asyncio.run(
        call_mcp_tool(
        state["project"],
        state["dataset"],
        state["table"],
        state["bucket"],
        ))


    state["execution_result"] = result
    state["logs"].append("Executor: Migration executed via MCP tool")
    state["status"] = "COMPLETED"
    return state