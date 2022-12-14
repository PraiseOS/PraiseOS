import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def exec(file):
    if os.name == 'nt':
        try:
            os.system(f'py {file}')
        except:
            os.system(f'python {file}')
    else:
        os.system(f'python3 {file}')