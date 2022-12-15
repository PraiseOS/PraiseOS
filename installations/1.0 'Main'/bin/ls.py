
import os, sys

def run(dir):
    try: dir
    except: os.listdir(); return;

    os.listdir(sys.argv[1])