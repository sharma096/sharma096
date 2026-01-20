import streamlit as st
from graph import migration_graph


st.title("GCP BigQuery → GCS Migration Agent")


project = st.text_input("GCP Project ID")
dataset = st.text_input("BigQuery Dataset")
table = st.text_input("BigQuery Table")
bucket = st.text_input("GCS Bucket")


if st.button("Start Migration"):
    state = {
    "project": project,
    "dataset": dataset,
    "table": table,
    "bucket": bucket,
    "plan": None,
    "validation": None,
    "execution_result": None,
    "logs": [],
    "status": "STARTED"
    }


    result = migration_graph.invoke(state)


    st.subheader("Status")
    st.write(result["status"])


    st.subheader("Report")
    st.write(result.get("report", "No report generated"))


    st.subheader("Logs")
    for log in result["logs"]:
        st.write(log)