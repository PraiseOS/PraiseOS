import os

def run(cmd):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')