#!/usr/bin/python3
"""Retrieves and sets the size of a square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializer.
        Args.
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
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square"""

        return (self.__size * self.__size)
