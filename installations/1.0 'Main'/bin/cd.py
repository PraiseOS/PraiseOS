import os

def run(cmd):
    try:os.chdir(cmd.removeprefix('cd ').replace('"', '').removesuffix('cd'))
    except:print(f'{dir} does not exist.')