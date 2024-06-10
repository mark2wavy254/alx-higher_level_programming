#!/usr/bin/python3
"""This module defines a square and returns the area"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializor.
        Args.
            size(int): length of the side of a square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def get_size(self):
        """Fetches the size of the square"""

        return self.__size

    def set_size(self, value):
        """sets the size of the square"""

        self.__size = value

    def area(self):
        """Returns the area of the square"""

        return (self.__size * self.__size)
