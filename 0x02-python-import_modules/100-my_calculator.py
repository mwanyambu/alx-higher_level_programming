#!/usr/bin/python3
from calculator_1 import add, mul, sub, div
import sys


def main():
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = ['+', '-', '*', '/']
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if operator == '+':
        result = add(a, b)
    if operator == '-':
        result = sub(a, b)
    if operator == '*':
        result = mul(a, b)
    if operator == '/':
        result = div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
