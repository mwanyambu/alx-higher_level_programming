#!/usr/bin/python3


def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(isinstance(row, list) and all(isinstance(x, (int, float)) for x in row) for row in matrix):
        raise TypeError("matarix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("each row of the matrix must have the same size")
    if not isinstance(div, int):
        raise TypeError("div must be an integer")

    final = []
    for row in matrix:
        rw = [round(x / div, 2) for x in row]
        final.append(rw)

    return final


