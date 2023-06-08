#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    count = len(argv)

    if count != 4:
        print("Usage: {} <a> <operator> <b>".format(a, b, argv[0]))
        exit(1)
        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])

        def invalid_operator():
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

        def addition():
            c = add(a, b)
            print("{} + {} = {}".format(a, b, c))
            return c

        def subtraction():
            d = sub(a, b)
            print("{} - {} = {}".format(a, b, d))
            return d

        def multiplication():
            e = mul(a, b)
            print("{} * {} = {}".format(a, b, e))
            return e

        def division():
            f = div(a, b)
            print("{} / {} = {}".format(a, b, f))
            return f

        options = {
                "+": addition,
                "-": subtraction,
                "*": multiplication,
                "/": division
        }
        options.get(operator, invalid_operator)()
