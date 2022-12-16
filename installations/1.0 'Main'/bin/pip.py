import os

def run(cmd):
    os.system(cmd.replace('pip', 'pip3'))