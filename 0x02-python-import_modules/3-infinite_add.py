#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    output = 0

    for argument in sys.argv[1:]:
        output += int(argument)
    print(output)
