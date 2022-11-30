from Modules import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists(functions.FILE_PATH):
    with open(functions.FILE_PATH,'w') as file:
        pass

#To make an executable:
#pyinstaller --onefile --windowed --clean gui.py

#sg.theme("DarkAmber")
#sg.theme("DarkPurple4")
#sg.theme("Black")
sg.theme("DarkBlue4")

clock = sg.Text('',key="clock")
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip= "Enter todo",key = "todo")
add_button = sg.Button("Add",size=10)
todos = functions.get_todos()
list_box = sg.Listbox(values=todos, key='todos',
                      enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")

window = sg.Window('My Todo App',
                   layout=[
                   [clock],
                   [label],
                   [input_box, add_button],
                   [list_box, edit_button, complete_button],
                   [exit_button]
                   ],
                   font=('Helvetica', 12))
while 1:

    event, values = window.read(timeout=1000)#milliseconds
    window["clock"].update(value=time.strftime('%B %d %Y %I:%M:%S %p'))
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
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first",font=('Helvetica,12'))
                #print("Please select an item first")
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first",font=('Helvetica,12'))
                #print("Please select an item first")
        case "Exit":
            break
        case "todos":
            window['todo'].update(value = values['todos'][0])
        case sg.WIN_CLOSED:
            break



window.close()




