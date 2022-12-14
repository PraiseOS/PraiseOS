import getpass, hashlib

from simple_term_menu import TerminalMenu
from art import tprint

import os, time, utils, sys

utils.clear()

tprint('PraiseOS')

print('='*48)

print('\n\nРⷬrͬaͣiͥs͛eͤOͦS͛ Login Page\n')

print('(HELP): (Use UP and DOWN keys to make a selection. \n Once you are ready, press ENTER to finalise your choice)\n')

users = os.listdir('../../global/users')

users.append('Create New')

urname = users[TerminalMenu(users).show()]

if urname == 'Create New':
    os.system('python3 setup.pyw')
    sys.exit()

with open(f'../../global/users/{urname}/.pass') as f:
    paswrd = f.read()

tries = 0

while True:
    utils.clear()

    tprint('PraiseOS')

    print('='*48)

    print('\n\nРⷬrͬaͣiͥs͛eͤOͦS͛ Login Page\n')

    print(f'(HELP): (Type in the passcode to account "{urname}")\n')

    getpas = getpass.getpass('Passcode ?: ')

    encpass = hashlib.sha256(getpas.encode()).hexdigest()

    if encpass == paswrd:
        break
    elif tries == 3:
        utils.clear()
        for i in range(0,15):
            print(f'NO TRIES LEFT WAIT {15-i} MORE SECONDS')
            time.sleep(1)
        tries = 0
    else:
        utils.clear()
        print('Incorrect Password')
        time.sleep(2)
        tries += 1

os.system('python3 home.py')