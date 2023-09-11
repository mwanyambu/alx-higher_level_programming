#!/usr/bin/python3

"""classMyInt defined"""


class MyInt(int):
    """invert operators"""
    def __ne__(self, value):
        """invert != with =="""
        return self.real == value

    def __eq__(self, value):
        """invert == with !="""
        return self.real != value
