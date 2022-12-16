import os

def description():
    return "Installs Python Librarys"

def run(cmd):
    os.system(cmd.replace('pip', 'pip3'))