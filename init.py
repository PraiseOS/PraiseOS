import os, time, random

from colorama import Fore, init

os.system('clear')

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
    'O Found device Samsung_SSD_850_PRO_512GB SYSTEM.',
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

os.system('python3 bootscreen.pyw')