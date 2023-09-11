#!/usr/bin/python3

"""defines class square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square that inherits from rectangle"""

    def __init__(self, size):
        """size instantation and validation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        calculates area of a square
        returns area
        """
        return self.__size ** 2
