import os

def description():
    return "Clears The Console"

def run(cmd):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')