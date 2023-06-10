#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    num = len(argv)

    if num != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    def invalid_operator():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    def addition():
        result = add(a, b)
        print("{:d} + {:d} = {:d}".format(a, b, result))
        return result

    def subtraction():
        result = sub(a, b)
        print("{:d} - {:d} = {:d}".format(a, b, result))
        return result

    def multiplication():
        result = mul(a, b)
        print("{:d} * {:d} = {:d}".format(a, b, result))
        return result

    def division():
        result = div(a, b)
        print("{:d} / {:d} = {:d}".format(a, b, result))
        return result

    options = {
        "+": addition,
        "-": subtraction,
        "*": multiplication,
        "/": division
    }
    options.get(operator, invalid_operator)()
