import os
import PySimpleGUIQt as sg

def make_file_python(ProjectName): #function to make python project
    os.makedirs('../' + ProjectName)
    open(f"..\{ProjectName}\start.py", 'x')
def make_file_webapp(ProjectName): #function to make webapp project
    os.makedirs('../' + ProjectName)
    open(f"..\{ProjectName}\index.html", 'x')
    open(f"..\{ProjectName}\style.css", 'x')
    open(f"..\{ProjectName}\script.js", 'x')

sg.change_look_and_feel('DarkAmber') #colour

#layout of window
layout = [
    [sg.Text('File Types')],
    [sg.Radio('Python file (start.py)', 1, key='-PY-')],
    [sg.Radio('Web app (script.js, index.html, styles.css)', 1, key='-WEB-')],
    [sg.Text('Project Name: '), sg.InputText(key='-NAME-')],
    [sg.Button('Ok'), sg.Button('Cancel')],
]

window = sg.Window('Project Creator', layout) #make the window

while True:
    event, values = window.read()
    ProjectName = values['-NAME-']
    if event in (None, 'Cancel'):
        break
    if values['-PY-'] and ProjectName:
        make_file_python(ProjectName)
        break
    elif values['-WEB-'] and ProjectName:
        make_file_webapp(ProjectName)
        break

window.close()


