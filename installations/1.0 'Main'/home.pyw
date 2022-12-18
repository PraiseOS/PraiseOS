import sys, os, socket

from colorama import Fore, init
from commandhandler import check

with open(f'{sys.argv[0]}/.pass') as f:
    paswrd = f.read()

if not sys.argv[1] == paswrd:
    sys.exit()

init()

while True:
    try: check(input(f'{Fore.RED}{sys.argv[1]}@{socket.gethostname()}: {os.getcwd()}>{Fore.WHITE}'), sys.argv[1]) 
    except (KeyboardInterrupt): pass