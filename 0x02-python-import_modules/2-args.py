#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_num = len(sys.argv) - 1
    if arg_num == 0:
        print("0 argument.")
    elif arg_num == 1:
        print("{} argument.".format(arg_num))
    else:
        print("{} arguments.".format(arg_num))
    for a, argument in enumerate(sys.argv[1:], start = 1):
        print("{}: {}".format(a, argument))
