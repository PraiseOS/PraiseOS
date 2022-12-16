import os

def run(cmd):

    file = cmd.removeprefix('cat ').replace('"', '').removesuffix('cat')

    if not os.path.exists(file):
        print('Could not find file')
        return

    with open(file) as f:
        text = f.read()

    print(text)