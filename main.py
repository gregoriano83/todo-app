# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%d %b %Y %H:%M:%S ")
while True:
    print('It is', now)
    # Get user input and strip space chars from it
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # List comprehension
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(index+1, '.', item)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) - 1

            todos = functions.get_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:]) - 1

            todos = functions.get_todos()

            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            functions.write_todos(todos)

            message = f'Todo {todo_to_remove} was removed from the list.'
            print(message)
        except IndexError:
            print('There is no item with that number.')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid. ')

print('Bye!')
