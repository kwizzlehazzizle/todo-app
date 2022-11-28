import PySimpleGUI as sg
from ZipCreator import make_archive

label1 = sg.Text("Select files to compress")
input1 = sg.Input(tooltip= "Select directory")
choose_button1 = sg.FilesBrowse("Choose",key="files")

label2 = sg.Text("Select destination folder")
input2 = sg.Input(tooltip= "Select directory")
choose_button2 = sg.FolderBrowse("Choose",key="folder")

compress_button = sg.Button("Compress")
outputlabel = sg.Text(key="output", text_color='green')

window = sg.Window('File Compressor', layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button,outputlabel]])

while 1:
    event,values = window.read()
    print(event)
    print(values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths,folder)
    window["output"].update(value="Compression completed")
    for value in values:
        print(value,' : ',values[value])
    match event:
        #case "Compress":

        case sg.WIN_CLOSED:
            break


window.close()
