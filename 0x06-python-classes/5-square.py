#!/usr/bin/pyhton3
"""This module defines a square's size, area and prints '#'"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializer.
        Args:
            size(int): length of the side of a square.
        """

        self.__size = size

    @property
    def size(self):
        """Retrieves the size"""
        
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size"""

        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character '#' """

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
