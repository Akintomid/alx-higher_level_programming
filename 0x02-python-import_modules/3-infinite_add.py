#!/usr/bin/python3

import sys
output = 0

for argument in sys.argv[1:]:
    output += int(argument)
print(output)
