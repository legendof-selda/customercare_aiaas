from joji.portal import db
import streamlit as st

conn = db.get_connection()

with st.form("new_project") as form:
    project_name = st.text_input("Project_name", placeholder="A unique project name which can be used.")
    submit = st.form_submit_button("Create")

if submit and project_name:
    project_id = db.add_project(project_name, 0, conn)
    st.write(f"{project_name}[{project_id}] created!")

try:
    projects = db.get_all_projects(0, conn)
    st.table(projects)
except Exception as e:
    st.error(e)
