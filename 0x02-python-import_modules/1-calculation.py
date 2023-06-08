#!/usr/bin/python3
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div

a = 10
b = 5

output = add(a, b)
print("{} + {} = {}".format(a, b, output))


output = sub(a, b)
print("{} - {} = {}".format(a, b, output))

output = mul(a, b)

print("{} * {} = {}".format(a, b, output))

output = div(a, b)

print("{} / {} = {}".format(a, b, output))
