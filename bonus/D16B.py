import PySimpleGUI as sg

# define the window's contents
layout = [[sg.Text("Select files to compress"), sg.Input(key='-FILE-'), sg.FilesBrowse('Choose')],
          [sg.Text("Select destination folder"), sg.Input(key='-DEST-'), sg.FolderBrowse('Choose')],
          [sg.Button('Compress')]]

# Create the window
window = sg.Window('File Compressor', layout)

# Display and interact with the Window using an Event Loop
while True:

    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()