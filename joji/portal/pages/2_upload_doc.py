from joji.portal import db
import re
import streamlit as st
from io import StringIO
import openai
import json

conn = db.get_connection()


@st.cache_data
def markdown_to_embeddings(markdown_string, project_id):
    print("generating embeddings")
    c = conn.cursor()
    # Remove markdown formatting
    text = re.sub("[^a-zA-Z0-9 \n\.]", "", markdown_string)
    # Generate embeddings
    embeddings = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=[text],
    )["data"][
        0
    ]["embedding"]
    emb_str = json.dumps(embeddings)
    # delete if exists
    c.execute("DELETE FROM embedding where project_id = ?", (project_id,))
    # Insert embeddings into database
    c.execute("INSERT INTO embedding (project_id, text_embedding) VALUES (?, ?)", (project_id, emb_str))
    conn.commit()
    return emb_str


with st.form("lookup_project_form"):
    projects_df = db.get_all_projects(0, conn)
    projects = dict(zip(projects_df["project_id"], projects_df["name"]))
    project_id = st.selectbox(
        "Select project:", projects_df["project_id"].to_list(), format_func=lambda x: projects[x], key="project"
    )
    uploaded_files = st.file_uploader("Troubleshoot doc", type=["md"], accept_multiple_files=True)
    submit_button = st.form_submit_button("Upload troubleshoot document")

if project_id and uploaded_files and submit_button:
    text = ""
    for uploaded_file in uploaded_files:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        text = text + stringio.read()

    emb = markdown_to_embeddings(text, project_id)

    with st.expander("Preview Embedding", False):
        st.write(f"Project: {project_id}")
        st.write(json.loads(emb))
