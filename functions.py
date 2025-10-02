def get_todos(filepath="todos.txt"):
    """Read a text file and return the list of
       todo items in that file.
    Args:
        filepath (str, optional): _description_. Defaults to "data/todos.txt".
    Returns:
        _type_: _description_
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return [todo.strip() for todo in todos_local if todo.strip()]


def write_todos(todos_arg, filepath="todos.txt"):
    """write the todo items list in the text file
    Args:
        todos_arg (_type_): _description_
        filepath (str, optional): _description_. Defaults to "data/todos.txt".
    """
    with open(filepath, "w") as file:
        file.writelines(todo + "\n" for todo in todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
