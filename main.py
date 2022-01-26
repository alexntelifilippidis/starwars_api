# hello!!
# for cache you have to keep json or create or run in terminal python main.py cache --clean
# for the question 4 i create a viem method.run in terminal python main.py view "luke"

import sys
from defs import cache, search, print_data, view


if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[2] == '--clean':
            globals()[sys.argv[1]](sys.argv[2], True)
        else:
            globals()[sys.argv[1]](sys.argv[2])
    if len(sys.argv) == 4:
        if sys.argv[3] == '--world':
            globals()[sys.argv[1]](sys.argv[2], True)
