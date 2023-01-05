import sys, os, socket, utils

from colorama import Fore, init
from commandhandler import check

with open(f'../../global/users/{sys.argv[1]}/.pass') as f:
    paswrd = f.read()

if not sys.argv[2] == paswrd:
    sys.exit()

init()

while True:
    try: check(input(f'{Fore.RED}{sys.argv[1]}@{socket.gethostname()}: {os.getcwd()}>{Fore.WHITE}'), sys.argv[1]) 
    except (KeyboardInterrupt): utils.clear(); sys.exit();