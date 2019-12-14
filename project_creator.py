import os
import PySimpleGUIQt as sg

sg.change_look_and_feel('DarkAmber') #colour

#layout of window
layout = [ 
    [sg.Text('File Types')],
    [sg.Text('1. Python file (start.py)')],
    [sg.Text('2. Web app (script.js, index.html, styles.css)')],
    [sg.Text('Choose your file type (1 or 2):'), sg.InputText()],
    [sg.Text('Project Name:'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')],
]
window = sg.Window('Project Creator', layout) #make the window

event, values = window.read()
ProjectName = values[1]

def make_file_python(ProjectName): #function to make python project
    os.makedirs('../' + ProjectName)
    open(f"..\{ProjectName}\start.py", 'x')
def make_file_webapp(ProjectName): #function to make webapp project
    os.makedirs('../' + ProjectName)
    open(f"..\{ProjectName}\index.html", 'x')
    open(f"..\{ProjectName}\style.css", 'x')
    open(f"..\{ProjectName}\script.js", 'x')

count = 0
while count < 1:
    if event in (None, 'Cancel'):
        break
    elif values[0] == '1':
        make_file_python(ProjectName)
        count +=1
    elif values[0] == '2':
        make_file_webapp(ProjectName)
        count +=1
    elif count >= 1:
        break

window.close()


