import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    if todo.strip():
        todos.append(todo)
        functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")

for index, todo in enumerate(todos):
    checkbox_value = st.checkbox(todo, key=todo)
    if checkbox_value:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(
    label="New todo",
    placeholder="Enter a todo...",
    label_visibility="collapsed",
    on_change=add_todo,
    key="new_todo",
)
