import os

def run(cmd):
    file = cmd.removeprefix('py ').replace('"', '').removesuffix('py')

    if os.name == 'nt':
        os.system(f'py {file}')
    else:
        os.system(f'python3 {file}')