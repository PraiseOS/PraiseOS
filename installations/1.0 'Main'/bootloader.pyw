from rich import *
from rich.console import Console

import os, time, tqdm

os.system('clear')

w, h = os.get_terminal_size()

console = Console()

def cprint(rgb=(255,255,255), text=""):
    console.print((' '*((w//2)-len(text)//2)+text), style=f"rgb({rgb[0]},{rgb[1]},{rgb[2]})")
    time.sleep(.5)

print('\n'*(h//2-4))

cprint(rgb=(255,255,0), text="██████╗░██████╗░░█████╗░██╗░██████╗███████╗░█████╗░░██████╗")
cprint(rgb=(255,255,0), text="██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔════╝")
cprint(rgb=(255,255,0), text="██████╔╝██████╔╝███████║██║╚█████╗░█████╗░░██║░░██║╚█████╗░")
cprint(rgb=(255,255,0), text="██╔═══╝░██╔══██╗██╔══██║██║░╚═══██╗██╔══╝░░██║░░██║░╚═══██╗")
cprint(rgb=(255,255,0), text="██║░░░░░██║░░██║██║░░██║██║██████╔╝███████╗╚█████╔╝██████╔╝")
cprint(rgb=(255,255,0), text="╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝░╚════╝░╚═════╝░")

print('\n'*(h//2-5))

data = range(69)
for _ in tqdm.tqdm(data):
    time.sleep(0.25)