#!/usr/bin/python3

""" Class Square definition"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """Create new Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The current area of the square."""
        return (self.__size * self.__size)
