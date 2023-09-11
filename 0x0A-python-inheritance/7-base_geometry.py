#!/usr/bin/python3

"""defines class BaseGeometry"""


class BaseGeometry:
    """class"""

    def area(self):
        """define area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        checks if value is an integer and raises typerror if not
        checks if value is > 0 and raises valueerror if not
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
