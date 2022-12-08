#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) < 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    opr = argv[2]
    if opr == "+":
        print("{} {} {} = {}".format(a, opr, b, add(a, b)))
    elif opr == "-":
        print("{} {} {} = {}".format(a, opr, b, sub(a, b)))
    elif opr == "*":
        print("{} {} {} = {}".format(a, opr, b, mul(a, b)))
    elif opr == "/":
        print("{} {} {} = {}".format(a, opr, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
