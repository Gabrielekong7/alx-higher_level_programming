#!/usr/bin/python3
"""Square module."""

class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Constructo.

        Args:
            size: Lenght of a side  of the square.

        Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise valueError('size must be >= 0')
        self.size = size
