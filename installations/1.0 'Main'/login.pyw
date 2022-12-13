import getpass, hashlib

from simple_term_menu import TerminalMenu
from art import tprint

import os

os.system('clear')

tprint('PraiseOS')

print('='*48)

print('\n\nРⷬrͬaͣiͥs͛eͤOͦS͛ Login Page\n')

print('(HELP): (Use UP and DOWN keys to make a selection. \n Once you are ready, press ENTER to finalise your choice)\n')

TerminalMenu(os.listdir('../../global/users')).show()