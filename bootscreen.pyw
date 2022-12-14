from rich import *
from rich.console import Console

import os, time, utils

w, h = os.get_terminal_size()

console = Console()

def cprint(rgb=(255,255,255), text=""):
    console.print((' '*((w//2)-len(text)//2)+text), style=f"rgb({rgb[0]},{rgb[1]},{rgb[2]})")
    time.sleep(.5)

for i in range(0,3):
    w, h = os.get_terminal_size()

    utils.clear()

    print('\n'*(h//2-4))

    time.sleep(.5)

    cprint(rgb=(255,255,0), text="██████╗░██████╗░░█████╗░██╗░██████╗███████╗░█████╗░░██████╗")
    cprint(rgb=(255,255,0), text="██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔════╝")
    cprint(rgb=(255,255,0), text="██████╔╝██████╔╝███████║██║╚█████╗░█████╗░░██║░░██║╚█████╗░")
    cprint(rgb=(255,255,0), text="██╔═══╝░██╔══██╗██╔══██║██║░╚═══██╗██╔══╝░░██║░░██║░╚═══██╗")
    cprint(rgb=(255,255,0), text="██║░░░░░██║░░██║██║░░██║██║██████╔╝███████╗╚█████╔╝██████╔╝")
    cprint(rgb=(255,255,0), text="╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝░╚════╝░╚═════╝░")

    time.sleep(.2)

time.sleep(1)

os.clear()

os.system('python3 bootmanager.pyw')