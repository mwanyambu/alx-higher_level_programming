#!/usr/bin/python3
from add_0 import add
"""import the add function from the add_0 module to perform addition"""
def main():
    a = 1
    b = 2
    print("{0} + {1} = {2}".format(a, b, add(a, b)))
if __name__ == "__main__":
    main()
