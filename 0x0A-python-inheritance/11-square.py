""" a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, a subclass of Rectangle."""

    def __init__(self, size):
        """Initialize a square with the given size.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: The square description in the format [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"
