import os, time, random, sys, json, utils

with open('data.json') as f:
    settings = json.load(f)

if not settings['USED']:
    settings['USED'] = True
    with open('data.json') as f:
        json.dump(settings)
    if os.name == 'nt':
        os.system('install.bat')
        sys.exit()
    else:
        os.system('bash install.sh')
        sys.exit()

from colorama import Fore, init

utils.clear()

w, h = os.get_terminal_size()
targets = [
    'O Create System Users.',
    'O Entropy Daemon based on the HAVEGE algorithm.',
    '# Starting Rule-based Manager for Device Events and Files.',
    'O Reached target Encrypting Volumes.',
    'O Listening on Process Core Dump Socket.',
    'O Reached target Remote File Systems.',
    'O Started Create list of required static device nodes.',
    'O Waiting for udev To Complete Device Initialization.',
    'O Monitoring of LVM2 mirrors, etc. using dmeventd or progress polling.',
    'O Started Apply Kernel Variables.',
    'O Mounted Debug File System.',
    'O Mounted Configuration File System.',
    'O Mount POSIX Message Queue File System.',
    'O Started Journal service.',
    'O Started Remount Root and Kernel File Systems.',
    '# Starting udev Coldplug all Devices...',
    '# Starting Flush Journal to Persistent Storage...',
    '# Starting Create Static Device Nodes in /dev...',
    '# Starting Load/Save Random Seed...',
    'O Started Load/Save Random Seed.',
    'O Started udev Coldplug all Devices.',
    'O Started Create Static Device Nodes in /dev.',
    '# Starting udev Kernel Device Manager...',
    'O Reached target Local File Systems (Pre).',
    'O Started Flush Journal to Persistent Storage.',
    'O Started udev Kernel Device Manager.',
    '# Mounting /boot...',
    '# Hello Youtube!'
]

def fancyboot():
    for target in targets:
        _ = target.split(' ')[0]
        if _ == 'O':
            print(f'[  {Fore.GREEN}' + 'OK' + f'{Fore.WHITE}  ] ' + target[2:])
        elif _ == '#':
            print(' '*9 + str(target[2:]))
        elif _ == 'F':
            print(f'[{Fore.RED}' + 'FAILED' + f'{Fore.WHITE}]' + target[2:])
        time.sleep(random.uniform(0.05, 0.07))
    time.sleep(0.07)

init()

fancyboot()

del targets

time.sleep(1)

utils.exec(f"bootscreen.pyw {settings['ADMIN']}")