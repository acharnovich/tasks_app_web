import streamlit
from modules import functions

tasks = functions.get_tasks()

def add_task():
    task = streamlit.session_state["new_task"] + "\n"
    tasks.append(task)
    functions.write_tasks(tasks)
    streamlit.session_state["new_task"] = ""

streamlit.title("The Task App!")
streamlit.subheader("Welcome to the task app.")
streamlit.write("This is a part of my Github portfolio")

for index, task in enumerate(tasks):
    checkbox = streamlit.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        functions.write_tasks(tasks)
        del streamlit.session_state[task]
        streamlit.rerun()

streamlit.text_input(label="", placeholder="Add a new task...",
                     on_change=add_task, key='new_task')
