import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo_ = st.session_state["new_todo"] + "\n"
    todos.append(todo_)
    functions.write_todos(todos)

st.title("My ToDo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label="Add new todo:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')