from langgraph.graph import StateGraph, END, START
from migrationai.agents.planner import planner_agent
from migrationai.agents.validator import validator_agent
from migrationai.agents.reporter import reporter_agent
from migrationai.agents.executor import executor_agent
from state.agentstate import MigrationState

workflow = StateGraph(MigrationState)

workflow.add_node("planner", planner_agent)
workflow.add_node("validator", validator_agent)
workflow.add_node("executor", executor_agent)

workflow.add_node("reporter", reporter_agent)

workflow.set_entry_point("planner")
workflow.add_edge("planner", "validator")
workflow.add_edge("validator", "executor")
workflow.add_edge("executor", "reporter")
workflow.add_edge("reporter", END)

migration_graph = workflow.compile()