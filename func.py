# This creates the function called get_todo which gets the file which holds the list and opens it as a read file.
# Functions reduce redundant code
# This is a constant
FILEPATH = "todos.txt"


def get_todo(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# This code will only be executed if this file is run. if it is run through another program, this won't run
# if we print(__name__) we can see that this variable is defined as __main__, but if it is run through main.py
# then the value will be called func / whatever the file is called.
if __name__ == "__main__":
    print("Hello")
