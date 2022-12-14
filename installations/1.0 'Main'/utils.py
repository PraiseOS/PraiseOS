import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def exec(file):
    clear()
    if os.name == 'nt':
        os.system(f'py {file}')
    else:
        os.system(f'python3 {file}')
    clear()

def read_data():
    with open('../../data.json') as f:
        return f.read()

def get_id():
    id = os.getcwd().split('/')[-1]

    return id

id = get_id()