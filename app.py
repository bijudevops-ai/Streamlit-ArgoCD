
import streamlit as st
import psycopg2

st.title("PostgreSQL Connector App")

host = st.text_input("Host", "postgres-service")
dbname = st.text_input("Database", "postgres")
user = st.text_input("User", "postgres")
password = st.text_input("Password", type="password")

if st.button("Connect"):
    try:
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password
        )
        st.success("Connected to database!")
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        st.write("Server time:", result[0])
        cur.close()
        conn.close()
    except Exception as e:
        st.error(f"Connection failed: {e}")
