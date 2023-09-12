#!/usr/bin/python3

"""class student"""


class Student:
    """defines a class student"""

    def first_name(self):
        """define first_name"""

    def last_name(self):
        """define last_name"""

    def age(self):
        """define age"""

    def __init__(self, first_name, last_name, age):
        """instance of first_name and last_name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation of student"""

        if attrs is None:
            return self.__dict__
        x = {}
        for y in attrs:
            if y in self.__dict__:
                x[y] = self.__dict__[y]
        return x
