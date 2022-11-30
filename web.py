import streamlit as st
from Modules import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app")
for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="Add a new todo: ")