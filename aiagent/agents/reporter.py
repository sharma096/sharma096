from Client import client
from langchain_core.prompts import ChatPromptTemplate
from migrationai.state.agentstate import MigrationState

model = client

report_prompt = ChatPromptTemplate.from_template("""
   Generate a user friendly migration report.


   Plan: {plan}
   Validation: {validation}
   Execution Result: {execution_result}
   Logs: {logs}


   Include:
   - Summary
   - Warnings
   - Final status
   - GCS path
""")

def reporter_agent(state: dict):
   chain = report_prompt | model
   report = chain.invoke(state).content


   state["report"] = report
   return state