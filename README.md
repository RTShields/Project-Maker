# Project-Maker
Script is outdated and has been replaced with an EXE

Upon starting the program, you can input the project's NAME, DESCRIPTION, and any MODULES you'll need for your script. To see a demo of the program in action, while in the first text field, leave it blank and press ENTER to generate a demo project.

[Description]
You have the option of leaving this field blank, and it will leave the program to write a time stamp to the new file. Otherwise be sure to leave a string of at least four characters.

[Modules]
The following are acceptable as input:
"numpy"
"from numpy import *"
"numpy as np"
"numpy, scipy, etc"
If "import is detected without an accompanying "from" it will be removed for that section of the Modules variable.

[ ] Create Virtual Environmental Script
Creates virtual.bat and an acompanying readme, please consult that for instructions

[ ] Create Clean Code Checker Script
Creates a batch script that will make a Revision.txt with reports by PyCodeStyle and PyFlakes 

[ ] Create PyInstaller Script
To be run within the virtual environment, but can be run without. Creates a batch script to run the pyinstaller command and create a single file executable.
