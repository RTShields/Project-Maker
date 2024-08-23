#!/usr/bin/env python

"""----------------------------------------------------------------------------
- v3.0 created on 2023-04-06                                                  -
- A python project to help create future projocts a lot easier... hopefully.  -
-                                                                      ~ John -
----------------------------------------------------------------------------"""

from os import getcwd
from os import mkdir
from os import startfile as open_project_path
from os.path import isdir
from os.path import dirname
from os.path import abspath
from os.path import join
import datetime as dt
import sys
import PySimpleGUI as sg

# #------------------------------ Code Below ---------------------------------#


def resource_path(relative_path):
    """ Get absolute path to resource for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', dirname(abspath(__file__)))
    return join(base_path, relative_path)


def description_breakdown(desc):
    """ Break down the description into manageable chunks """
    desc_lines = []
    banner_breakdown = []
    word_bank = desc.split()
    line = ''

    for word in word_bank:
        if len(line + word) + 1 <= 75:
            line += f'{word} '
        else:
            desc_lines.append(line.strip())
            line = f'{word} '
    desc_lines.append(line.strip())

    for line in desc_lines:
        new_line = f'- {line}'
        while len(new_line) <= 77:
            new_line += ' '
        banner_breakdown.append(f'{new_line}-')

    return banner_breakdown


def description_banner(desc):
    """ Reconstructs the description string into something banner friendly """
    space_limit = 79
    banner = []

    dashes = ''
    while len(dashes) + 4 <= space_limit:
        dashes += '-'
    banner.append(f'"""{dashes}')

    now = str(dt.datetime.today())
    less_now = now[:now.find(' ')]
    creation_line = f'- Program created on {less_now}'
    while len(creation_line) <= space_limit - 2:
        creation_line += ' '
    banner.append(f'{creation_line}-')

    spacer_line = ''
    while len(spacer_line) <= space_limit - 3:
        spacer_line += ' '
    banner.append(f'-{spacer_line}-')

    signature = '-'
    sig = '~ Tech -'
    while len(signature) + len(sig) <= space_limit - 1:
        signature += ' '
    signature += sig

    if len(desc) + 4 <= space_limit:
        while len(desc) <= space_limit - 5:
            desc += ' '
        banner.append(f'- {desc} -')
    else:
        description_lines = description_breakdown(desc)
        for line in description_lines:
            banner.append(line)

    banner.append(f'-{spacer_line}-')
    banner.append(signature)
    banner.append(f'{dashes}"""')
    return banner


def python_to_exe(file_path, project):
    """ Create the pyinstaller batch script to convert the .py to .exe """
    with open(f'{file_path}/py_to_exe.bat', 'w', encoding='utf8') as tech:
        tech.write('@echo off\npip install -U pyinstaller\n:build\ncls\ndel ')
        tech.write('Revisions.txt\ndel *.rev\npyinstaller --onefile ^\n\t--n')
        tech.write('oconsole ^\n\t--distpath "Final Build" ^\n\t--workpath "')
        tech.write('TMP Files" ^\n\t--specpath "TMP Files" ^\n\t--clean ^\n')
        tech.write(f'\t{project}.py\npause\ncls\necho "Check out the ../TMP ')
        tech.write(f'Files/{project}/Warn-{project} file should issues arise')
        tech.write('."\necho "If using an icon, use --icon "../MyIcon.ico" ^')
        tech.write('"\necho " Resource: https://PyInstaller.org"\necho ""\ne')
        tech.write('cho "Hit any key to retry the build if there was an erro')
        tech.write('r somewhere."\npause\ngoto :build')
        tech.close()


def create_virtualpy(file_path, file_name):
    """ Create virtual Python enviornment management script """
    with open(f'{file_path}/{file_name}', 'w', encoding='utf8') as tech:
        tech.write('@echo off\nif "%1"=="-i" goto stepv1\nif "%1"=="-c" goto')
        tech.write(' stepv2\nif "%1"=="-a" goto stepv3\nif "%1"=="-r" goto s')
        tech.write('tepv4\nif "%1"=="/i" goto stepc1\nif "%1"=="/c" goto ste')
        tech.write('pc2\nif "%1"=="/a" goto stepc3\nif "%1"=="/u" goto updat')
        tech.write('e\nif "%1"=="-u" goto update\ngoto error\n\n:stepv1\n\tp')
        tech.write('ip install -U virtualenv\n\tgoto end\n\n:stepv2\n\tpytho')
        tech.write('n -m venv VirPy\n\tgoto end\n\n:stepv3\n\tVirPy/Scripts/')
        tech.write('activate\n\tgoto end\n\n:stepv4\n\tpip freeze --local > ')
        tech.write('Requirements.txt\n\tgoto end\n\n:stepc1\n\tpip install a')
        tech.write('uxlib\n\tpip install cytoolz\n\tpip install ruamel.yaml')
        tech.write('\n\tpip install conda\n\tgoto end\n\n:stepc2\n\tconda cr')
        tech.write('eate -n VirConda -y\n\tgoto end\n\n:stepc3\n\tactivate V')
        tech.write('irConda\n\tgoto end\n\n:update\n\tpip_modules.bat\n\tgot')
        tech.write('o end\n\n:error\n\tcls\n\techo Error: Invalid option. Pl')
        tech.write('ease us one of the following flags:\n\techo -i\t: Instal')
        tech.write('l virtualenv\n\techo -c\t: Create virtual envirnomnet Vi')
        tech.write('rPy\n\techo -a\t: Activate VirPy\n\techo -r\t: Generate ')
        tech.write('a Requirements doc for project modules\n\techo /i\t: Ins')
        tech.write('tall Conda\n\techo /c\t: Create the Conda virtual enviro')
        tech.write('nment VirConda\n\techo /a\t: Activate VirConda\n\techo /')
        tech.write('u\t: update current virtual environment with needed modu')
        tech.write('les\n\techo Please try again with an opened console\n\tp')
        tech.write('ause\n\n:end')
        tech.close()


def create_faqs(file_path):
    """ Create FAQs text doc for virtual instructions """
    with open(f'{file_path}/FAQs.txt', 'w', encoding='utf8') as tech:
        tech.write('Virtual Enviroment Scripts Instructions:\n')
        tech.write('Always use the following flags for Virtual Env:.\n')
        tech.write('-i\tInstall the wanted VirEnv.\n')
        tech.write('-c\tCreate the wanted VirEnv.\n')
        tech.write('-a\tActivate the VirEnv.\n')
        tech.write("\nThese flags are for use with Conda's virtual env:\n")
        tech.write("/i\tInstall Conda's virtual environment.\n")
        tech.write("/c\tCreate the VirConda virtual environment.\n")
        tech.write("/a\tActivate the VirConda virtual environment.\n\n")
        tech.write('-u\tUpdates either virtual environments\n and "')
        tech.write('install project modules\n')
        tech.close()


def create_virtual_bat(file_path):
    create_virtualpy(file_path, 'virtualpy.bat')
    create_faqs(file_path)


def create_revision_resort(file_path, project):
    """ Create python script to better organize Revision.txt """
    with open(f'{file_path}/repylint.py', 'w', encoding='utf8') as tech:
        tech.close()


def create_code_check(file_path, project):
    """ Create code style/formatting script """
    create_revision_resort(file_path, project)

    with open(f'{file_path}/code_check.bat', 'w', encoding='utf8') as tech:
        tech.write(f'@echo off\n:clean\npycodestyle --ignore=501 {project}.p')
        tech.write(f'y > pycodestyles.rev\npyflakes {project}.py > pyflakes.')
        tech.write(f'rev\npylint {project}.py > pylint.rev\npython repylint.')
        tech.write('py\nECHO Complete, press any key to rerun scan.\npause\n')
        tech.write('goto :clean')
        tech.close()


def clean_modules_list_to_pip(modules, project_path):
    """ Clean up the modules list, create a pip installing .bat file """
    mods_to_pip = []
    unpip = ['collections', 'datetime', 'logging', 'math', 'numpy', 'os',
             'pip', 'sys', 'time']
    default_mods = ['numpy', 'scipy', 'matplotlib', 'pyinstaller', 'auxlib',
                    'cytoolz', 'ruamel.yaml', 'pycosat', 'pycodestyle',
                    'pyflakes', 'pylint']

    for mod in modules:
        if mod.find('.') != -1:
            mod = mod[:mod.find('.')]

        if mod.find(' as ') != -1:
            mod = mod[:mod.find(' as')]

        if mod.find('from') != -1:
            mod = mod.replace('from ', '')

        if mod.find(' import') != -1:
            mod = mod[:mod.find(' import')]

        if mod not in unpip and mod not in mods_to_pip:
            mods_to_pip.append(mod)

    for addon in default_mods:
        if addon not in mods_to_pip:
            mods_to_pip.append(addon)

    mods_to_pip.sort()

    with open(f'{project_path}/pip_modules.bat', 'w', encoding='utf8') as pip:
        pip.write('python -m pip install --upgrade pip\n\n')
        for module in mods_to_pip:
            pip.write(f'pip install -y {module}\n')
        pip.close()


def get_modules(mods, project_path):
    """ Grab the module string, and organize them for import and pip'ing """
    mods = mods.replace(', ', ',')
    mods_split = mods.split(',')
    modules = []
    mods_import = []

    for module in mods_split:
        if module.find('from') != -1:
            modules.append(module)
        elif module.find('import') != -1:
            mods_import.append(module.replace('import ', ''))
        elif module.find('.') != -1:
            pass
        else:
            mods_import.append(module)

    modules.sort()
    mods_import.sort()

    for module in mods_import:
        modules.append(module)

    clean_modules_list_to_pip(modules, project_path)

    return modules


def create_python_project(values):
    """ Take the GUI inputs and craft the python program & supporting items"""
    project_name = values['proj_name']
    project_path = f'Projects/{project_name}'
    project_description = values['proj_desc']
    project_modules = values['proj_mods']

    if project_path.find('Projects/') != -1 and isdir('Projects/') is False:
        mkdir('Projects')

    if isdir(project_path) is False:
        mkdir(project_path)

    project_file = f'{project_path}/{project_name}.py'
    with open(project_file, 'w', encoding='utf8') as tech:
        tech.write('#!/usr/bin/env python\n\n')

        if len(project_description) > 0:
            banner = description_banner(project_description)
            for line in banner:
                tech.write(f'{line}\n')
            tech.write('\n')

        if len(project_modules) > 0:
            mods = get_modules(project_modules, project_path)
            for line in mods:
                if line.find('from') != -1:
                    tech.write(f'{line}\n')
                else:
                    tech.write(f'import {line}\n')

        space = '=============================='
        tech.write(f'\n# #{space}= Code Below {space}# #\n')

        tech.close()

        create_virtual_bat(project_path)
        python_to_exe(project_path, project_name)
        create_code_check(project_path, project_name)
        root = getcwd().replace('\\', '/')
        open_project_path(f'{root}/{project_path}/')


def portable_appinfo():
    """ Create docs for PortableApps """
    print('creating appinfo.ini')
    if isdir('App') is False:
        mkdir('App')

    if isdir('App/AppInfo') is False:
        mkdir('App/AppInfo')

    with open('App/AppInfo/appinfo.ini', 'w', encoding='utf8') as tech:
        tech.write('[Format]\nType=PortableApps.comFormat\nVersion=3.0\n')
        tech.write('\n[Details]\nName=Python Project Creator\nAppID=Pyth')
        tech.write('onProjectCreator\nPublisher=John Palmer\nCategory=De')
        tech.write('velopment\nDescription=Python script maker\nLanguage')
        tech.write('=English\n\n[License]\nShareable=true\nOpenSource=Fa')
        tech.write('lse\nFreeware=true\nCommercialUse=true\n\n[Version]=')
        tech.write('PackageVersion=2023.4.10.0\nDisplayVersion=2023-04-1')
        tech.write('0\n\n[Control]\nIcons=1\nStart=Python Project Creato')
        tech.write('r.exe\nBaseAppID=%BASELAUNCERPATH%\\APP\\PythonProje')
        tech.write('ctCreator\\bin\\Python Project Creator.exe\n\n[Assoc')
        tech.write('iations]\nFileTypes=py')
        tech.close()


def squirrel_demo():
    """ Demo to demonstrate the program's usefulness. """
    values = {
        'proj_name': 'squirrels',
        'proj_desc': 'Create a powerful Squirrel AI',
        'proj_mods': 'squirrels, from nuts import pecan, sys, os'}
    create_python_project(values)


def menu_simplegui():
    """ GUI menu for creating scripts """
    sg.theme('DarkBlue')

    layout = [
        [sg.Text('Project Name:', size=(20, 1))],
        [sg.InputText(key='proj_name')],

        [sg.Text('Project Description:', size=(20, 1))],
        [sg.Multiline(key='proj_desc', size=(43, 4))],

        [sg.Text('List of Modules, Separated by commas', size=(28, 1))],
        [sg.Multiline(key='proj_mods', size=(43, 4))],

        [sg.Push(), sg.Submit(), sg.Button('DEMO'), sg.Cancel(), sg.Push()],
        [sg.Push(), sg.Button('P.AppsInfo'), sg.Push()]]

    title = 'Python Project Creator v3.0'
    icon = 'I:/Documents/Coding/0_personal/Python Project Crafter/python.ico'
    window = sg.Window(title, icon=resource_path(icon)).Layout(layout)
    events, values = window.read()

    while True:
        if events == 'Cancel':
            break

        if events == 'DEMO':
            squirrel_demo()
        elif events == 'Submit':
            create_python_project(values)
        elif events == 'P.AppsInfo':
            portable_appinfo()

        break


menu_simplegui()
