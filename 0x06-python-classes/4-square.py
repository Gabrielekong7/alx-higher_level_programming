#!/usr/bin/python3
"""Square module."""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Lenght of a side of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise  TypeError("size must be an integer")
            if value < 0:
                raise a ValueError('size must be >= 0')
            self._size = value

        def area(self):
            """Area of this square.

            Returns:
                "The size squared
            """
            return self.__size ** 2

