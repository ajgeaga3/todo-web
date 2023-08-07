import streamlit as st
import functions

# Check if 'todos' is already in session state. If not, initialize it with the values fetched from the functions.get_todos() function.
if 'todos' not in st.session_state:
    st.session_state.todos = functions.get_todos()


# Define a function to add a new todo item.
def add_todo():
    # Append the new todo with a newline character to the todos list in session state.
    todo = st.session_state.new_todo + "\n"
    st.session_state.todos.append(todo)

    functions.write_todos(st.session_state.todos)

    # Clear the text input field by setting the session state 'new_todo' key to an empty string.
    st.session_state.new_todo = ""



st.title("To-Do List")


st.write("What do you got going on today?")

# Create an empty list to collect indices of todo items that should be removed.
items_to_remove = []

# Loop through each todo item in session state's todos list.
for index, todo in enumerate(st.session_state.todos):
    # Display a checkbox for each todo item. The key ensures each checkbox is unique.
    checkbox = st.checkbox(todo, key=f"{index}, {todo}")

    # If the checkbox is checked, add its index to the items_to_remove list.
    if checkbox:
        items_to_remove.append(index)

# Remove checked todo items from the session state's todos list.
for index in reversed(items_to_remove):
    # Remove the todo item at the specified index.
    popped_todo = st.session_state.todos.pop(index)

    # Save the updated todos list.
    functions.write_todos(st.session_state.todos)

    # If the removed todo item has a corresponding key in session state, delete that key.
    if popped_todo in st.session_state:
        del st.session_state[popped_todo]

    # Rerun the app to immediately reflect the removal of the todo item in the UI.
    st.experimental_rerun()

# Display a text input field for adding new todo items.
# When the content of the input changes (i.e., a new todo is entered), the add_todo function is called.
st.text_input(label="", placeholder="Add todo here", on_change=add_todo, key='new_todo')
