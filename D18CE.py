import functions
import PySimpleGUI as sg
import time

sg.theme('DarkTeal3')
# Define the window's contents
layout = [[sg.Text('', key='-CLOCK-')],
          [sg.Input(size=(30, 5),key='-INPUT-'),
          sg.Button(size=3, image_source='add.png', tooltip='Add todo', key='Add')],
          [sg.Listbox(size=(30, 5), key='-TODOS-', values=functions.get_todos(), enable_events=True)],
           [sg.Button('Show'),
           sg.Button('Edit'),
           sg.Button(size=3, image_source='complete.png', tooltip='Complete todo', key='Complete'),
           sg.Button('Quit')],
          [sg.Text(size=(30, 1), key='-OUTPUT-')]]

# Create the window
window = sg.Window('Todo App',
                   layout,
                   font=("Helvetica", 20))

now = time.strftime("%b %d, %Y %H:%M:%S")

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read(timeout=100)
    window['-CLOCK-'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    if event == 'Add':
        new_todo = values['-INPUT-'] + '\n'
        todos = functions.get_todos()
        todos.append(new_todo)

        functions.write_todos(todos)

        todos = functions.get_todos()
        window['-TODOS-'].update(values=todos)
    elif event == 'Edit':
        try:
            todos = functions.get_todos()
            todo_to_edit = values['-TODOS-'][0]
            index = todos.index(todo_to_edit)
            new_todo = values['-INPUT-']+'\n'
            todos[index] = new_todo
            functions.write_todos(todos)
            window['-TODOS-'].update(values=todos)
        except IndexError:
            sg.popup('Please select todo to edit', font=("Helvetica", 20))
    elif event == '-TODOS-':
        window['-INPUT-'].update(values['-TODOS-'][0].strip('\n'))
    elif event == 'Complete':
        try:
            todos = functions.get_todos()
            completed_todo = values['-TODOS-'][0]
            todos.remove(completed_todo)
            functions.write_todos(todos)
            window['-INPUT-'].update(value='')
            window['-TODOS-'].update(values=todos)
        except IndexError:
            sg.popup('Please select todo to edit', font=("Helvetica", 20))

# Finish up by removing from the screen
window.close()

