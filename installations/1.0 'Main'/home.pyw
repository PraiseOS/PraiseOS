import sys, os, socket, utils, hashlib

from colorama import Fore, init
from commandhandler import check

with open(f'../../global/users/{sys.argv[1]}/.pass') as f:
    paswrd = f.read()

encpass = hashlib.sha256(sys.argv[2].encode()).hexdigest()

if not encpass == paswrd:
    sys.exit()

init()

os.chdir(f'../../global/users/{sys.argv[1]}/main')

dir = os.getcwd()

while True:
    try: check(input(f'{Fore.RED}{sys.argv[1]}@{socket.gethostname()}: {os.getcwd().replace(dir, "") if len(os.getcwd().replace(dir, "")) != 0 else "~"}/>{Fore.WHITE}'), sys.argv[1]) 
    except (KeyboardInterrupt): utils.clear(); sys.exit();