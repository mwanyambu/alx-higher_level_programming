#!/usr/bin/python3

"""defines class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle that inherits from BaseGeometry"""

    def area(self):
        """
        define area
        return area of rectangle
        """
        return self.__width * self.__height

    def __init__(self, width, height):
        """instantation of width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
