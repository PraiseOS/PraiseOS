from bin import *
from bin import __all__
import os

ops  = ['+', '-', '/', '*', '^', '**']
cmds = ['file-explorer', 'pkgm-gui', './', 'tree', 'dir', 'ls', 'add-package', 'text-editor']

def check(cmd, usr):
    math = 0
    for op in ops:
        if op in cmd:
            try:
                math = 1
                exec(f'print(str({cmd}).split(\'.\')[0])')
                break
            except (NameError, SyntaxError):
                math = 0
    if cmd.lower() == "":
        pass
    elif cmd.lower().startswith("dir") or cmd.lower().startswith("ls"):
        ls.listdirectory(''.join(cmd.split(' ')[1:]), usr)
    else:
        if math == 0:print("Command not found run help for list of commands")
        math = 1