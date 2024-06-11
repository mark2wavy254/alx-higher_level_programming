#!/usr/bin/python3
"""Defines a square by size and position"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializer.
        Args:
            size(int): length of the side of a square
            position(tuple): position of the square
        """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieves the size"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets the size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """retrieves the position"""

        return self.__position

    @position.setter
    def position(self, value):
        """sets the position"""

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """returns the area of the square"""

        return (self.__size * self.__size)

    def my_print(self):
        """prints the square using the '#' symbol """

        if self.__size == 0:
            print("")
            return

        [print("", end="") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print("#", end="") for j in range(0, self.__size)]
            print("")
