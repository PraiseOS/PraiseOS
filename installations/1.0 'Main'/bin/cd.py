import os

def description():
    return "Changes The Current Directory"

def run(cmd):
    dir = cmd.removeprefix('cd ').replace('"', '').removesuffix('cd')

    try:os.chdir(dir)
    except:print(f'{dir} does not exist')