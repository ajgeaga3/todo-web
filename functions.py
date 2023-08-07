def get_todos(path="todos.txt"):
    """Gets todos by reading the file and returning the todo-list."""
    with open(path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, path="todos.txt"):
    """Writes the todos by writing the to-do list in the file."""
    with open(path, 'w') as file:
        file.writelines(todos_arg)

