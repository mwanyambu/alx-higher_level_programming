#!/usr/bin/python3

"""class student"""


class Student(object):
    """defines a class student"""

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
        for k, v in self.__dict__.items():
            if k in attrs:
                x[k] = v
        return x

    def reload_from_json(self, json):
        """replace all attrs of student"""
        for k, v in json.items():
                setattr(self, k, v)
