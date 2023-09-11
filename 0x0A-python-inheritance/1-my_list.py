#!/usr/bin/python3

"""define class Mylist"""


class MyList(list):
    """class inherits from list"""

    def print_sorted(self):
        """prints a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
