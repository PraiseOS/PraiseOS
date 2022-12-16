import os

def run(cmd):
    os.system(cmd.removeprefix('system '))