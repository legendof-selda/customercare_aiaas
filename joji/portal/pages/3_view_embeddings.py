from joji.portal import db
import streamlit as st
import json

conn = db.get_connection()

with st.form("lookup_project_form"):
    projects_df = db.get_all_projects(0, conn)
    projects = dict(zip(projects_df["project_id"], projects_df["name"]))
    project_id = st.selectbox(
        "Select project:", projects_df["project_id"].to_list(), format_func=lambda x: projects[x], key="project"
    )
    submit_button = st.form_submit_button("View Embedding!")

if project_id and submit_button:
    result = db.get_project_embedding(project_id, conn)
    st.subheader(f"{result[1]}[{result[0]}]")
    st.write(json.loads(result[-1]))
