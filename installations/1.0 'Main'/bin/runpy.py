import os

def description():
    return "Uses The Python Interpreter To Execute Python Files"

def run(cmd):
    file = cmd.removeprefix('runpy ').replace('"', '').removesuffix('runpy')

    print(os.path.abspath(file))

    if not os.path.exists(os.path.abspath(file)):
        print('Could Not Find File')
        return

    if os.name == 'nt':
        os.system(f'py {file}')
    else:
        os.system(f'python3 {file}')