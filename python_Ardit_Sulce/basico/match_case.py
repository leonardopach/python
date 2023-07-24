

user_action = input("Type add, show, or exit: ")

todos: list[str] = []
while True:
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
