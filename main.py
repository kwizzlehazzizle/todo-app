#filepath = 'Files/todos.txt'
#from functions import get_todos, write_todos

from Modules import functions
import time

message = "Hello, choose either 'add','show', 'edit' , 'complete' or 'exit' :"
now = time.strftime('%B %d %Y %I:%M:%S %p')
print("It is currently ",now)

while 1:

    user_action = input(message).strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo.capitalize())

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        print("Hello there, don't forget to do the following today:")
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{int(index+1)}-{item}")

    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos()


            number = int(user_action[5:])
            number = number - 1

            newTodo = input("Enter new todo item: ")
            todos[number] = newTodo + '\n'


            functions.write_todos(todos)
        except ValueError:
            print("You done goofed! Value Error. You need to input an integer after edit. Ex: edit 2")
            continue
    elif user_action.startswith('complete'):
        try:
            numberToRemove = int(user_action[9:])

            todos = functions.get_todos()

            index = numberToRemove-1
            todoToRemove = todos[index].strip('\n')
            print(todoToRemove, ' was removed.')

            todos.pop(index)
            functions.write_todos(todos)
        except IndexError:
                print("There is no entry with that number")
                continue


    elif user_action.startswith('exit'):
        break
    else:
        print('Unknown Command!')



print("Bye!")




