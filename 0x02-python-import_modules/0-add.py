#!/usr/bin/python3
from add_0 import add as ab
a = 1
b = 2

add_code = """
def add(a, b):
    return a + b
"""
exec(add_code)

output = ab(a, b)
print("{} + {} = {}".format(a, b, output))
