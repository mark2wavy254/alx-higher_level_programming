#!/usr/bin/python3
"""This module defines a square using a private attribute"""


class Square:
    """defines a square"""

    def __init__(self, size):
        """Initialization
        Args:
            size: length of the sides of a square
        """

        self.__size = size
