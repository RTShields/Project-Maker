# Convert Python to EXE
# This program takes pyinstaller and converts any other python script
# into an exe file with or without a provide Icon *.ico file. It will
# also clean up after itself once the process is complete and leave
# the end product *.exe file in the same directory as the script.

import os
import shutil
import glob
import subprocess
import sys


py_file = glob.glob('*.py')
icon_file = glob.glob('*.ico')

for files in py_file:
    if files == 'Converter.py':
        pass
    else:
        file = files

pypath = sys.path
path = pypath[5]
Core_path = path[:-13] + 'scripts\\'
Project_path = os.path.dirname(os.path.abspath(__file__)) + '\\'


def Move_PyInstaller(Core, Project):
    script = 'pyinstaller.exe'
    rFrom = Core + script
    rTo = Project + script
    try:
        shutil.copy(rFrom, rTo)
    except NotFound:
        print('Error moving PyInstaller.exe')


def Convert(file):
    global icon_file
    global Project_path
    with open('convert.bat', 'w') as con:
        if len(icon_file) == 0:
            con.write('pyinstaller -w -F -i ' + file)
        else:
            icon = icon_file[0]
            con.write('pyinstaller -w -F -i "' + icon + '" "' + file + '"')
        con.close
    subprocess.call('convert.bat')
    exfile = file[:-3] + '.exe'
    Dist_path = Project_path + 'dist\\' + exfile
    try:
        shutil.move(Dist_path, Project_path + exfile)
    except NotFound:
        print("Can't find executable.")


def cleanup():
    garbage = ['__pycache__', 'build', 'dist']
    bags = [file[:-3] + '.spec', 'pyinstaller.exe', 'convert.bat']
    try:
        for bag in garbage:
            shutil.rmtree(bag)
        for trash in bags:
            os.remove(trash)
    except NotFound:
        print('All Clean!')


Move_PyInstaller(Core_path, Project_path)
Convert(file)
cleanup()
