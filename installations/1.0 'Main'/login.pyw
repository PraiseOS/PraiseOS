import getpass, hashlib

from simple_term_menu import TerminalMenu
from art import tprint

import os

os.system('clear')

tprint('PraiseOS')

print('='*48)

print('\n\nРⷬrͬaͣiͥs͛eͤOͦS͛ Login Page\n')

print('(HELP): (Use UP and DOWN keys to make a selection. \n Once you are ready, press ENTER to finalise your choice)\n')

urname = os.listdir('../../global/users')[TerminalMenu(os.listdir('../../global/users')).show()]

with open(f'../../global/users/{urname}/.pass') as f:
    paswrd = f.read()

os.system('clear')

tprint('PraiseOS')

print('='*48)

print('\n\nРⷬrͬaͣiͥs͛eͤOͦS͛ Login Page\n')

print(f'(HELP): (Type in the passcode to account "{urname}")\n')

getpas = getpass.getpass('Passcode ?: ')

encpass = hashlib.sha256(getpas.encode()).hexdigest()

if encpass == paswrd:
    print('Hello')