import os, json

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
    #clear()

def read_data():
    with open('../../data.json') as f:
        settings = json.load(f)

def get_id():
    id = os.getcwd()#.split('/')[-1]

    return id

id = get_id()