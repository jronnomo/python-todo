def get_todos(filepath_arg):
    with open(filepath_arg, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(filepath_arg, todos_arg):
    with open(filepath_arg, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    filepath = 'todos.txt'
    todos = get_todos(filepath)
    print(f"Here are your todos {todos}")
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos(filepath)
        todos.append(todo + '\n')

        write_todos(filepath, todos)

    elif user_action.startswith('show'):
        todos = get_todos(filepath)

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}) {item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            todo_index = int(user_action[5:])-1
            todos = get_todos(filepath)
            print("Your current todos are:" + '\n' + f"{todos}")
            new_todo = input(f"What do you want to replace {todos[todo_index]} with?: ")
            todos[todo_index] = new_todo + '\n'
            write_todos(filepath, todos)
            print("Your new list of todos are:" + '\n' + f"{todos}")
        except ValueError:
            print("Please enter a command verb followed by a number")
    elif user_action.startswith('complete'):
        try:
            todos = get_todos(filepath)
            todo_index = int(user_action[9:])-1
            completed_task = todos[todo_index].strip('\n')
            todos.pop(todo_index)
            write_todos(filepath, todos)
            print(f"Successfully completed {completed_task}")
        except IndexError:
            todo_request = user_action[9:]
            print(f"There's no task {todo_request} in the list")
        except ValueError:
            print("Not a valid request. Please retry.")
    elif user_action.startswith('exit '):
        break
    else:
        print("This command is not valid")

print("Bye")