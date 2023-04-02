from joji.portal import db
import re
import streamlit as st
from io import StringIO
import openai

conn = db.get_connection()


def markdown_to_embeddings(markdown_string, project_id):
    c = conn.cursor()
    # Remove markdown formatting
    text = re.sub("[^a-zA-Z0-9 \n\.]", "", markdown_string)
    # Generate embeddings
    embeddings = (
        openai.Completion.create(
            engine="davinci",
            prompt=text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        .choices[0]
        .text
    )
    # Insert embeddings into database
    c.execute("INSERT INTO embeddings (project_id, text_embedding) VALUES (?, ?)", (project_id, embeddings))
    conn.commit()
    return embeddings.strip()


with st.form("lookup_project_form"):
    projects_df = db.get_all_projects(0, conn)
    projects = dict(zip(projects_df["project_id"], projects_df["name"]))
    project_id = st.selectbox(
        "Select project:", projects_df["project_id"].to_list(), format_func=lambda x: projects[x], key="project"
    )
    uploaded_files = st.file_uploader("Troubleshoot doc", type=["md"], accept_multiple_files=True)
    submit_button = st.form_submit_button("Select project")

if project_id and uploaded_files and submit_button:
    text = ""
    for uploaded_file in uploaded_files:
        text += uploaded_file.read()

    markdown_to_embeddings(text, project_id)
