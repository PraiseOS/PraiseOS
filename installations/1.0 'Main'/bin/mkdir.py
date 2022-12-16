import os

def description():
    return "Creates A Directory"

def run(cmd):
    dir = cmd.removeprefix('mkdir ').replace('"', '').removesuffix('mkdir')
    if not os.path.exists(dir):
        os.mkdir(dir)
    else:
        print(f'{dir} Already Exists')