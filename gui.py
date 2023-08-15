import functions
import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("Type add, show, edit, complete, or exit: ")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Add'),
           sg.Button('Show'),
           sg.Button('Edit'),
           sg.Button('Complete'),
           sg.Button('Quit')]]

# Create the window
window = sg.Window('Todo App', layout)

# Display and interact with the Window using an Event Loop
while True:
    todos = functions.get_todos()
    todos_display = []
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    if event == 'Add':
        user_action = values['-INPUT-'].strip()
        todo = user_action

        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)

        todos = functions.get_todos()
        functions.display_todos(window, todos)

    elif event == 'Edit':
        user_action = values['-INPUT-'].strip()
        todo = user_action


# Finish up by removing from the screen
window.close()

