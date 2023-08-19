import streamlit as st
import functions

st.title("Todo App")
st.subheader("This is my todo app")
st.write("Some random")

todos = functions.get_todos()

new_todo = st.text_input(label="Todo Input Label", placeholder="Add a todo here", label_visibility='hidden')


while True:
    if new_todo != "":
        try:
            todos.append(new_todo)
            functions.write_todos(todos)
            st.checkbox(new_todo)
        except:
            pass

