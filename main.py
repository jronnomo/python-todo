while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Add a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}) {item}"
                print(row)
        case 'edit':
            num_todo = int(input("What number todo to be edited?: "))-1
            old_todo = todos[num_todo]
            new_todo = input(f"What would you like to replace {old_todo} with?: ")
            todos[num_todo] = new_todo
            print(f"Successfully replaced {old_todo} with {new_todo}")
        case 'complete':
            todo_index = int(input("What number todo did you complete?: "))-1
            completed_task = todos[todo_index]
            todos.pop(todo_index)
            print(f"Successfully completed {completed_task}")
        case 'exit':
            break
        case _:
            print("Underscore is global known else case")

print("Bye")