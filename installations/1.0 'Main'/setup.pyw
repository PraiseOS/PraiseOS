import os, utils, sys, getpass, hashlib

from art import tprint

while True:
    utils.clear()

    tprint('PraiseOS')

    print('='*48)

    print('\n\nРⷬrͬaͣiͥs͛eͤOͦS͛ USER SETUP PAGE\n')

    print('(HELP): (Enter username and password to procede.)\n')

    urname = input('Enter Username: ')
    paswrd = getpass.getpass('Enter Password: ')
    cpas = getpass.getpass('Confirm Password: ')

    q = input('\nAre You Sure? (y/n): ')

    if cpas == paswrd and q == 'y':
        break

os.chdir('../../global/')

if not os.path.exists(os.getcwd()+'/users'):
    os.mkdir('users')

os.chdir('users')

os.mkdir(urname)

encpass = hashlib.sha256(paswrd.encode()).hexdigest()

with open(f'{urname}/.pass', 'w') as f:
    f.write(encpass)

os.chdir(f'../../installations/{utils.id}')

print(os.getcwd())