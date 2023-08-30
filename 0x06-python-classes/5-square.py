#!/usr/bin/python3

"""class square defines a square"""


class Square:
    """initial definition"""

    def area(self):
        """calculates and returns area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """size of the square"""
        return self.__size

    def __init__(self, size=0):
        """initialize size"""
        self.__size = size

    @size.setter
    def size(self, value):
        """
        set size and modify value
        raise errors if value is not int or less than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints area with # symbols"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                print("#" * self.__size)
