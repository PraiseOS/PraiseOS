import sys, os

from commandhandler import check

while True:
    check(input(f'{sys.argv[1]}>'), sys.argv[1])