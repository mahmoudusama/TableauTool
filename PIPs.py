import subprocess
import sys

def install(package_1,pacakege_2):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_1, package_2])


install('customtkinter')

#install('--upgrade','pip')


#pip install --upgrade pip


# pip install selenium==4.2.0

