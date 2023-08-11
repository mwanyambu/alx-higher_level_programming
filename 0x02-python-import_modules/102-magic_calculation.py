#!/usr/bin/python3
from calculator_1 import add, sub


def magic_calculation(a, b):
    if a < b:
        res = add(a, b)
        for i in range(4, 6):
            res = add(add, i)
        return res
    else:
        return sub(a, b)
