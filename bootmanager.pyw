from pick import pick

from art import tprint

import os, utils, time

tprint('PraiseOS')

print('='*48)

print('\n\nРⷬrͬaͣiͥs͛eͤOͦS͛ OS SELECTION\n')

print('(HELP): (Use UP and DOWN keys to make a selection. \n Once you are ready, press ENTER to finalise your choice)\n')

installations = os.listdir('installations')

large_i = installations

sp = []

for i in installations:
    try:
        sp.append(' '+i.split(' ')[1])
    except:
        sp.append('')
    large_i[installations.index(i)] = i.split(' ')[0]

for i in installations:
    installations[installations.index(i)] += sp[installations.index(i)]

installations[large_i.index(max(large_i))] = installations[large_i.index(max(large_i))] + ' - Recommended'

time.sleep(3)

choice = installations[pick(installations, indicator='>')[1]].replace(' - Recommended', '')

utils.clear()

os.chdir(os.getcwd()+f"/installations/{choice}/")

utils.exec(f'"bootloader.pyw"')