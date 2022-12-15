import os

def chdir(cmd):
    dir = ''

    dir_list = cmd.replace('"', '').split(' ')

    del dir_list[0]

    for i in dir_list:
        dir += i

    try:os.chdir(dir)
    except:print(f'{dir} does not exist.')