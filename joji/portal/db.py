import sqlite3
import streamlit as st
import pandas as pd
import os


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        st.write(e)

    return conn


def initialize_db(conn):
    c = conn.cursor()

    # Create table to store embeddings
    c.execute("CREATE TABLE IF NOT EXISTS user (user_id INTEGER PRIMARY KEY, user_name TEXT, pwd TEXT)")
    c.execute("""CREATE TABLE IF NOT EXISTS project (project_id INTEGER PRIMARY KEY, user_id INTEGER, name TEXT)""")
    c.execute(
        """CREATE TABLE IF NOT EXISTS embedding
                (project_id INTEGER PRIMARY KEY, text_embedding TEXT)"""
    )


def get_connection():
    conn = create_connection("joji.db")
    initialize_db(conn)
    return conn


def get_project_id(project_name, conn) -> int:
    # Retrieve project ID from database
    c = conn.cursor()
    c.execute("SELECT project_id FROM project WHERE name=?", (project_name,))
    row = c.fetchone()
    if row:
        return int(row[0])
    else:
        return None


def get_all_projects(user_id, conn) -> pd.DataFrame:
    c = conn.cursor()
    query = c.execute("SELECT project_id, name, user_id FROM project WHERE user_id=?", (user_id,))
    cols = [column[0] for column in query.description]
    results_df = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    return results_df


def add_project(project_name, user_id, conn) -> int:
    c = conn.cursor()
    # Insert project into database
    c.execute("INSERT INTO project (name, user_id) VALUES (?, ?)", (project_name, user_id))
    conn.commit()

    return get_project_id(project_name, conn)
