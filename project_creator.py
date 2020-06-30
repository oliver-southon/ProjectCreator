import os
import PySimpleGUIQt as sg

def make_file_python(ProjectName): #function to make python project
    os.makedirs('../' + ProjectName)
    open(f"..\{ProjectName}\start.py", 'x')
def make_file_webapp(ProjectName): #function to make webapp project
    projectPath = '../../WebApps/' + ProjectName
    os.makedirs(projectPath)
    os.makedirs(projectPath + '/resources/css/img')
    open(f"../../WebApps/{ProjectName}/resources/css/style.css", 'x')
    os.makedirs(projectPath + '/resources/data')
    os.makedirs(projectPath + '/resources/img')
    os.makedirs(projectPath + '/resources/js')
    os.makedirs(projectPath + '/vendors/css')
    os.makedirs(projectPath + '/vendors/fonts')
    os.makedirs(projectPath + '/vendors/js')
    open(f"../../WebApps/{ProjectName}/index.html", 'x')
    open(f"../../WebApps/{ProjectName}/style.css", 'x')

sg.change_look_and_feel('DarkBlue1') #colour

#layout of window
layout = [
    [sg.Text('File Types')],
    [sg.Radio('Python file (start.py)', 1, key='-PY-')],
    [sg.Radio('Web app', 1, key='-WEB-')],
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


