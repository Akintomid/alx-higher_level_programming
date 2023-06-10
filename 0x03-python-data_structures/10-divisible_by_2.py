#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    output = []
    for a in my_list:
        output.append(a % 2 == 0)
    return output
