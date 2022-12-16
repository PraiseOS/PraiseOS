import os

def description():
    return "Runs Commands On The Host Computer's Terminal"

def run(cmd):
    os.system(cmd.removeprefix('system '))