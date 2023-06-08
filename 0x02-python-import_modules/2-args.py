#!/usr/bin/python3

import sys
arg_num = len(sys.argv) - 1

if arg_num == 0:
    print("0 arguments.")
else:
    print("{} arguments.".format(arg_num))

for a, argument in enumerate(sys.argv[1:]):
    print("{} : {}".format(a, argument))
