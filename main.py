while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
            file.write(f'{todo}'+'\n')
    elif user_action.startswith('show'):
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}) {item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            todo_index = int(user_action[5:])-1
            print(todo_index)
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            print("Your current todos are:" + '\n' + f"{todos}")
            new_todo = input(f"What do you want to replace {todos[todo_index]} with?: ")
            todos[todo_index] = new_todo + '\n'
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            print("Your new list of todos are:" + '\n' + f"{todos}")
        except ValueError:
            print("Please enter a command verb followed by a number")
    elif user_action.startswith('complete'):
        try:
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            print(f"Current todos {todos}")
            todo_index = int(user_action[9:])-1
            completed_task = todos[todo_index].strip('\n')
            todos.pop(todo_index)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            print(f"Successfully completed {completed_task}")
        except IndexError:
            todo_num = int(user_action[9:])
            print(f"There's no task {todo_num} in the list")
    elif user_action.startswith('exit '):
        break
    else:
        print("This command is not valid")

print("Bye")