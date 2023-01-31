#!/usr/bin/python3
"""
A module for working with rectangles.
"""


class Rectangle:
    """
    Represents a 2D polygon with 4 perpendicular sides.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with a given width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            str: A string representatio of this rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ''
        else:
            s = str(self.print_symbol)
            w = self.width
            h = self.height
            res = map(lambda x: (s * w) + ('\n' * (x != h - 1)), range(h))
            return ''.join(list(res))

    def __repr__(self):
        """
        Returns a representation of this rectangle.
        Returns:
            str: A string representation of this rectangle.
        """
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        """
        Performs some routines after an object is deleted.
        """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area.
        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a new rectangle with equal width and height.
        Args:
            size (int): The width and height of the rectangle.
        Returns:
            Rectangle: The new rectangle with equal sides.
        """
        return Rectangle(size, size)
