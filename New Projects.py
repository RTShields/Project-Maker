# New Project Generator
# Creates a folder, initial script file, and codestyle checker
# for said script, then the pyinstaller converter

import os
import shutil
import glob
import sys
import re


def Link_strip(link):
    if link.find(' ') != -1:
        spaces = True
        step1 = link.replace(' ','_')
    else:
        spaces = False
        pass 

    if link == sys.executable:
        step2 = len(step1) - 10  # Removes 'python.exe' from link
        step3 = re.escape(step1[:step2])
    else:
        step3 = re.escape(step1)

    if spaces is True:
        step4 = step3.replace('_',' ')
    else:
        pass

    return step4


def Create_stuff(file, desc):
    # Create folder and file for the project
    pyfile = file + '\\' + file + '.py'
    print(pyfile)

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


def Crafter_checkers(file):
    # Move CodeStyle and PyFlakes to folder, creater checker script
    dist = Link_strip(sys.executable)
    scripts_path = dist + 'Scripts\\'
    scripts = ['pyinstaller.exe', 'pycodestyle.exe', 'pyflakes.exe', 'Converter.py']

    make_mods = 0
    for item in scripts:
        file_check = scripts_path + item
        if os.path.isfile(file_check) is False:
            make_mods += 1
        else:
            make_mods += 0

    if make_mods >= 1:
        ModInstaller()

    for item in scripts:
        shutil.copy(scripts_path + item, file + '\\' + item)

    with open(file + '\\checker.bat', 'w') as king:
        king.write('pycodestyle --ignore=E501 "' + file + '.py">Revisions.txt\n')
        king.write('pyflakes "' + file + '.py >> Revisions.txt')


def Main():
    #work_file = input('What is the name of the porject?')
    #desc = input('Describe what this script does:\n')
    work_file = 'Modules'
    desc = 'This script runs through a predefined list of python modules and creates a batch file to pip install each one.'
    Create_stuff(work_file, desc)  # File / Folder / Description
    Crafter_checkers(work_file)  # File / Folder / Python Script folder


Main()
  
