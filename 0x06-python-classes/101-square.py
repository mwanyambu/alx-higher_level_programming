#!/usr/bin/python3

"""a class square"""


class Square:
    """defines a square"""

    def area(self):
        """calculates and returns the area of a square"""
        return self.__size * self.__size

    @property
    def size(self):
        """size of square"""
        return self.__size

    def __init__(self, size=0, position=(0, 0)):
        """initializes the size and position"""
        self.size = size
        self.position = position

    @size.setter
    def size(self, value):
        """
        modifies value
        raise and error if value is not an int or less than
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints the position"""
        if self.__size == 0:
            print()
            return

        for x in range(self.__position[1]):
            print()

        for x in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """string representation of square"""
        if self.__size == 0:
            return ""

        sq = ""
        for y in range(self.__position[1]):
            sq += "\n"
        for y in range(self.__size):
            sq += " " * self.__position[0] + "#" * self.__size + "\n"
        return sq.rstrip()
