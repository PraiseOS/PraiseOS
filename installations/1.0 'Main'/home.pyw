import sys, os, socket

from colorama import Fore, init
from commandhandler import check

init()

while True:
    try: check(input(f'{Fore.RED}{sys.argv[1]}@{socket.gethostname()}: {os.getcwd()}>{Fore.WHITE}'), sys.argv[1]) 
    except (KeyboardInterrupt): pass