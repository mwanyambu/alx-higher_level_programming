#!/usr/bin/python3

"""a class square that defines a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """property to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """"modify value and
            raise errors if value is not an int or is less than 0"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates and returns area of a square"""
        return self.__size ** 2
