import sys, os, socket

from colorama import Fore, init
from commandhandler import check

init()

while True:
    check(input(f'{Fore.RED}{sys.argv[1]}@{socket.gethostname()}: {os.getcwd()}>{Fore.WHITE}'), sys.argv[1]) 