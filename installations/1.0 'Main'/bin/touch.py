import os

def description():
    return "Creates A File"

def run(cmd):
    file = cmd.removeprefix('touch ').replace('"', '').removesuffix('touch')

    if os.path.exists(file):
        print('File Already Exists')
        return

    with open(file, 'w') as f:
        pass