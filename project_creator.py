import os
import PySimpleGUIQt as sg

sg.change_look_and_feel('DarkAmber') #colour

#layout of window
layout = [
[sg.Frame(layout=[
    [sg.Checkbox('1. Python file (start.py)', default=False,key='pyfile'),
     sg.Checkbox('2. Web app (script.js, index.html, styles.css)', default=False,key='webapp')]],
title='Select File Type from the Checkbox',title_color='red', 
relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
[sg.Text('Project Name:'), sg.InputText()],
[sg.Submit(), sg.Button('Cancel')],
]

window = sg.Window('Project Creator', layout) #make the window

event, values = window.read()
ProjectName = values[0]

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
    elif values['pyfile'] == True:
        make_file_python(ProjectName)
        count +=1
    elif values['webapp'] == True:
        make_file_webapp(ProjectName)
        count +=1
    elif count >= 1:
        break

window.close()


