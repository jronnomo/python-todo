todos = []

while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Add a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            num_todo = int(input("What number todo to be edited?: ")) - 1
            old_todo = todos[num_todo]
            new_todo = input("What would you like to replace this todo with?: ")
            todos[num_todo] = new_todo
            print(f"replaced {old_todo} with {new_todo} successfully")
        case 'exit':
            break
        case _:
            print("Underscore is global known else case")

print("Bye")