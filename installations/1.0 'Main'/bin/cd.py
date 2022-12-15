import os

def chdir(cmd):
    dir = ''

    dir_list = cmd.replace('"', '').split(' ')

    del dir_list[0]

    for i in dir_list:
        dir += i

    os.chdir(dir)