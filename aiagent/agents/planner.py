from Client import client
from langchain_core.prompts import ChatPromptTemplate
from migrationai.state.agentstate import MigrationState

model = client

planner_prompt = ChatPromptTemplate.from_template("""
You are a data migration planner

Input:
Project: {project}
Dataset: {dataset}
Table: {table}

Decide:
- export_format(parquet or csv)
- load_type (full vs incremental)
- partition_strategy (none/ ingestion_date / column)

Return JSON:
{{
"export_format": "parquet",
"load_type": "full",
"partition_strategy": "none"
}}

""")

def planner_agent(state: MigrationState) -> MigrationState:
    chain = planner_prompt | model
    result = chain.invoke(state).content

    state["plan"] = eval(result)
    state["logs"].append("Planner: Migration plan created")
    return state