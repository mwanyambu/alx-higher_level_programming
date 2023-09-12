#!/usr/bin/python3

"""pascal triangle"""


def pascal_triangle(n):
    """define pascal triangle"""
    if n <= 0:
        return ""

    pastr = [[1]]

    for x in range(1, n):
        row = [1]
        y = pastr[x - 1]
        for i in range(1, x):
            row.append(y[i] + y[i - 1])
        row.append(1)
        pastr.append(row)
    return pastr
