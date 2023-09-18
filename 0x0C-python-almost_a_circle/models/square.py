#!/usr/bin/python3

from models.rectangle import Rectangle

"""class square"""


class Square(Rectangle):
    """class square inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update square"""
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
        """dictionary representation of square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
            }

    def __str__(self):
        """returns string representation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
