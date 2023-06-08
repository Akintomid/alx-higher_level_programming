#!/usr/bin/python3

a = 10
b = 5

from calculator_1 import add

output = add(a, b)
print("{} + {} = {}".format(a, b, output))

from calculator_1 import sub

output = sub(a, b)
print("{} - {} = {}".format(a, b, output))

from calculator_1 import mul

output = mul(a, b)

print("{} * {} = {}".format(a, b, output))

from calculator_1 import div

output = div(a, b)

print("{} / {} = {}".format(a, b, output))
