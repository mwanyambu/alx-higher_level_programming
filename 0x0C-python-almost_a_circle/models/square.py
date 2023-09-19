#!/usr/bin/python3

from models.rectangle import Rectangle


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
        self.size = size

    def __str__(self):
        """
        Returns a string representation of square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """get size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        """set size of a square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes of a square
        Args:
            *args: positional arguments for updating attributes
            **kwargs: keyword argument for updating attributes

        """
        if args and len(args) != 0:
            j = 0
            for a in args:
                if j == 0:
                    if a is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = a
                elif j == 1:
                    self.size = a
                elif j == 2:
                    self.x = a
                elif j == 3:
                    self.y = a
                j += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Returns a dictionary representation of square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
            }
