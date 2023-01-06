import sys, os

def description():
    return "Exits This Active Session"

def run(cmd):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    sys.exit()