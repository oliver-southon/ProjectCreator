#1. user enters name of project
#2. determine type (python or web)
#3. If python makes a dir with project name in Projects folder, plus start.py
#3. If web, makes dir w/ projectname and files: scipt.js, index.html, styles.css

import os
import PySimpleGUI as sg
FileName = input('Project name: ')
print('Select file type:\n1. Python \n2. Web app')
ProjectType = input('Type: ')

def make_file(x):
    if x == '1':
        os.makedirs('../' + FileName)
        open(f"..\{FileName}\start.py", 'x')
    elif x == '2':
        os.makedirs('../' + FileName)
        open(f"..\{FileName}\index.html", 'x')
        open(f"..\{FileName}\style.css", 'x')
        open(f"..\{FileName}\script.js", 'x')

make_file(ProjectType)
path = os.getcwd()

#ProjectName = input("Enter the project name: ")

