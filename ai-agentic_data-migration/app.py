# import streamlit as st
# from orchestor import run_migration

# st.title("🤖 Agentic AI Data Migration (Free LLM)")

# project = st.text_input("Project ID")
# dataset = st.text_input("Dataset")
# table = st.text_input("Table")

# request = st.text_area(
#     "Migration Intent",
#     "Export this dataset for analytics usage"
# )

# if st.button("Run Migration"):
#     with st.spinner("AI agents working..."):
#         result = run_migration(request, project, dataset, table)

#     if result["status"] == "BLOCKED":
#         st.error("Migration Blocked")
#         st.json(result)
#     else:
#         st.success("Migration Completed")
#         st.json(result["plan"])
#         st.write(result["report"])



import streamlit as st
from orchestrator import run_pipeline
st.title("Agentic AI Data Migration")
intent = st.text_area("Describe your migration intent")
if st.button("Run Migration"):
   with st.spinner("Running agentic pipeline..."):
       output = run_pipeline(intent)
   st.success("Completed")
   st.write(output)