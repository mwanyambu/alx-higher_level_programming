#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for row in matrix:
        rows_squared = [i**2 for i in row]
        squares.append(rows_squared)
    return squares
