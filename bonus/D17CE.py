import PySimpleGUI as sg

def convertToMeters(feet, inches):
    return (feet + inches/12) * 0.3048


layout = [[sg.Text('Enter Feet', key="foot_label"), sg.Input(key="foot_input")],
          [sg.Text('Enter Inches', key="inch_label"), sg.Input(key="inch_input")],
          [sg.Button("Convert", key="convert_button"), sg.Text(key="_OUTPUT_")]]

window = sg.Window("Converter", layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    match event:
        case sg.WINDOW_CLOSED:
            break
        case 'convert_button':
            feet = int(values['foot_input'])
            inches = int(values['inch_input'])
            meters = convertToMeters(feet, inches)
            window['_OUTPUT_'].update(f"{meters}m")
    print(event, values)