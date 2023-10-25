#!/usr/bin/python3
"""Square module."""


class square:
    """ Define a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Lenght of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of the Square.

        Returns:
            the size squred.
        """
        return self.__size ** 2
