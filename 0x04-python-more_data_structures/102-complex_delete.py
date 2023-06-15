#!/usr/bin/python3
def complex_delete(my_dict, value):
    copy = my_dict.copy()
    for a, b in copy.items():
        if value in b:
            del my_dict[a]
    return my_dict
