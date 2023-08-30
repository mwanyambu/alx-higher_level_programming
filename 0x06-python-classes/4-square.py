#!/usr/bin/python3

"""a class square that defines a square"""


class Square:

    def area(self):
        """calculates the area of a square"""
        return self.__size * self.__size

    def size(self):
        """size of the square"""
        return self.__size

    @property
    def size(self):
        """property to retrieve size"""
        return self.__size

    def __init__(self, size=0):
        """initialization of size"""
        self.__size = size

    @size.setter
    def size(self, value):
        """"
        set size
        size must be an integer and not less than zero
        value must be an integer and not less than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
