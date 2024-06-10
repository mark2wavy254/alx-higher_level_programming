#!/usr/bin/python3
"""This module defines a square with a private instance attribute"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializor
        Args
            size: length of the side of a square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")

        self.__size = size
