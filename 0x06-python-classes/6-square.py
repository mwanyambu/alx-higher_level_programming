#!/usr/bin/python3
class Square:

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    def __init__(self, size=0, position=(0, 0)):
        self.__size = 0
        self.__position = (0, 0)
        self.size = size
        self.position = position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or 
                len(value) != 2 or 
                not all(isinstance(num, int) for num in value) or 
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for x in range(self.__position[1]):
            print()

        for x in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for x in range(self.__size):
                print("#", end="")
            print()
