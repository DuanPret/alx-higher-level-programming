#!/usr/bin/python3
"""
A module for working with rectangles.
"""


class Rectangle:
    """
    Represents a 2D polygon with 4 perpendicular sides.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with a given width and height.
        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of this rectangle.
        Returns:
            int: The width of this rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves the height of this rectangle.
        Returns:
            int: The height of this rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Updates the width of this rectangle.
        Args:
            value (int): The new width of this rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
         Updates the height of this rectangle.
         Args:
             value (int): The new height of this rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """
        Computes the area of this rectangle.
        Returns:
            int: The area of this rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes the perimeter of this rectangle.
        Returns:
            int: The perimeter of this rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of this rectangle.
        Returns:
            str: A string representation of this rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ''
        else:
            res = list(map(
                lambda x: '#' * self.width + '\n' * (x != self.height - 1),
                range(self.height)))
            return ''.join(res)
