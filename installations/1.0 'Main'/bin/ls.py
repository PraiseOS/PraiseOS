
import os, sys

try: sys.argv[1]
except: os.listdir(); sys.exit();

os.listdir(sys.argv[1])