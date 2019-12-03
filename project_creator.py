import os
import PySimpleGUIQt as sg

sg.change_look_and_feel('DarkAmber') #colour

#layout of window
layout = [ 
    [sg.Text('File Types')],
    [sg.Text('1. Python file (start.py)')],
    [sg.Text('2. Web app (script.js, index.html, styles.css)')],
    [sg.Text('Project Name:'), sg.InputText()],
    [sg.Text('File type: '), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')],
]
window = sg.Window('Peep', layout) #make the window

event, values = window.read()
FileName = values[0]

def make_file(x):
    if x == '1':
        os.makedirs('../' + FileName)
        open(f"..\{FileName}\start.py", 'x')
    elif x == '2':
        os.makedirs('../' + FileName)
        open(f"..\{FileName}\index.html", 'x')
        open(f"..\{FileName}\style.css", 'x')
        open(f"..\{FileName}\script.js", 'x')

count = 0
while True:
    if event in (None, 'Cancel'):
        break
    make_file(values[1])
    count +=1
    if count >= 1:
        break

window.close()
#ProjectName = input("Enter the project name: ")

