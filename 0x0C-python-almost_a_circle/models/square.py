#!/usr/bin/python3

from models.rectangle import Rectangle

"""defines a class square"""


class Square(Rectangle):
    """class representing a square that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize an instance of a square
        Args:
            size (int): size of a square
            y (int): y-coordinate
            x (int): x-coordinate
            id (int): identifier for the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes of a square
        Args:
            *args(int): positional arguments for updating attributes
            **kwargs(dict): keyword argument for updating attributes

        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for attribute, arg in enumerate(args):
                if attribute < len(attributes):
                    setattr(self, attributes[attribute], arg)

        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        Returns a dictionary representation of square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
            }

    def __str__(self):
        """returns the string representation of a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
