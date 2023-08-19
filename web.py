import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.write_todos(todos)


st.title("Todo App")
st.subheader("List of todos:")

for todo in todos:
    st.checkbox(todo)

new_todo = st.text_input(label="Todo Input Label",
                         placeholder="Add a todo here",
                         label_visibility='hidden',
                         on_change=add_todo,
                         key="new_todo")
