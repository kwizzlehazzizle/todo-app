from Modules import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip= "Enter todo",key = "todo")
add_button = sg.Button("Add")
todos = functions.get_todos()
list_box = sg.Listbox(values=todos, key='todos',
                      enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")

window = sg.Window('My Todo App',
                   layout=[
                   [label],
                   [input_box, add_button],
                   [list_box, edit_button, complete_button],
                   [exit_button]
                   ],
                   font=('Helvetica', 12))
while 1:
    event, values = window.read()
    print("Event: ", event)
    print("Values: ", values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Exit":
            break
        case "todos":
            window['todo'].update(value = values['todos'][0])
        case sg.WIN_CLOSED:
            break



window.close()




