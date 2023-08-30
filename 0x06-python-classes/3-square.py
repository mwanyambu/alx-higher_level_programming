#!/usr/bin/python3

"""a class square that defines a square"""
class Square:

    """
    area calculates the area of a square
    size: private instance attribute
    """

    def area(self):
        return self.__size * self.__size

    def __init__(self, size=0):


        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
