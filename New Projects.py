# New Project Generator
# Creates a folder, initial script file, and codestyle checker
# for said script, then the pyinstaller converter

import os
import shutil
import glob
import sys
import re


# find Python folder
dist = sys.executable
redist = dist.replace(' ', '_')
xout = len(dist) - 10
pydist = re.escape(redist[:xout])
f_pydist = pydist.replace('_', ' ')
print(f_pydist)
scripts = ['pyinstaller.exe', 'pycodestyle.exe', 'pyflakes.exe', 'Converter.py']

make_mods = 0
for item in scripts:
    file_check = f_pydist + 'Scripts\\\\' + item
    if os.path.isfile(file_check) is False:
        make_mods += 1
    else:
        make_mods += 0


def ModInstaller():
    with open('Modules Installer.bat', 'w') as Mods:
        if os.path.isfile(f_pydist + 'pyinstaller.exe') is False:
            Mods.write('pip install pyinstaller\n')
        if os.path.isfile(f_pydist + 'pycodestyle.exe') is False:
            Mods.write('pip install pycodestyle\n')
        if os.path.isfile(f_pydist + 'pyflakes.exe') is False:
            Mods.write('pip install pyflakes\n')
        if os.path.isfile(f_pydist + 'Converter.py') is False:
            Mods.write('Please copy/paste Converter.py manually.')
        Mods.close()
    return


if make_mods >= 1:
    ModInstaller()


def Create_stuff(file, Fpath, desc):
    # Create folder and file for the project
    pyfile = Fpath + '\\' + file + '.py'

    if os.path.isdir(file) is True:
        # Create the work folder
        folder2 = input('Project folder already exist, try another.\n')
        os.mkdir(folder2)
    else:
        os.mkdir(file)

    with open(pyfile, 'w') as creator:
        creator.write('# ' + file + '\n')
        creator.write('# Created by John Palmer\n')
        Tchar = len(desc)
        print(Tchar)
        if Tchar <= 60:
            creator.write('# ' + desc)
            creator.close()
        else:
            Tlines = 1 + int(Tchar / 60)
            lcount = 0
            for line in range(Tlines):
                pout = line * 60
                print(pout)

                creator.write('# ' + desc[pout:pout + 60] + '\n')
        creator.close()
    return


def Crafter_checkers(file, Fpath, PyPath):
    # Move CodeStyle and PyFlakes to folder, creater checker script
    global scripts
    for item in scripts:
        shutil.copy(PyPath + item, Fpath + item)

    with open(file + '\\checker.bat', 'w') as king:
        king.write('pycodestyle --ignore=E501 "' + file + '.py">Revisions.txt\n')
        king.write('pyflakes "' + file + '.py >> Revisions.txt')


def Main():
    work_file = input('What is the name of the porject?')
    desc = input('Describe what this script does:\n')
    # work_file = 'Python Breaker'
    # desc = '0123456789012345678901234567890123456798ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    folder_path = 'D:\\Documents\\Documents\\[-] Coding Projects\\-01- Work Scripts'
    dest_path = folder_path + '\\' + work_file
    py_path = pydist + 'Scripts\\'
    folder = folder_path + '\\' + work_file
    Create_stuff(work_file, dest_path, desc)
    Crafter_checkers(work_file, dest_path + '\\', py_path)


Main()
