import streamlit as st
import func

todo_list = func.get_todo()


def add_todo():
    todo_to_add = st.session_state["new_todo"] + "\n"
    todo_list.append(todo_to_add)
    func.write_todos(todo_list)


st.title("My Todo APP")
st.write("Your TO-DO list:")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=f"{todo}")
    if checkbox:
        todo_list.pop(index)
        func.write_todos(todo_list)
        del st.session_state[f"{todo}"]
        st.experimental_rerun()

st.text_input(label='', placeholder="Enter your new to-do item",
              on_change=add_todo, key="new_todo")
