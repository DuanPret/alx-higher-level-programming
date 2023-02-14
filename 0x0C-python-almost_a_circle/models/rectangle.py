#!/usr/bin/pytho3
""" Contains class Rectangle which implements Base. """
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle implements Base.
    Methods:
        __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the instance of the class. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter function for __width
        Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for width.
        Args:
            value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter function for height
        Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter function for height
        Args:
            value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Getter function for x.
        Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter function for x.
        Args:
            value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            getter function for y.
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter function for y.
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ Returns the area of the rectangle instance. """
        return (self.__width * self.__height)

    def display(self):
        """ Prints to stdout the Rectangle instance with '#' symbol. """
        rectangle = ""
        print_symbol = "#"

#        for i in range(self.__height - 1):
#            rectangle += print_symbol * self.__width + "\n"
#        rectangle += print_symbol * self.__width

#       print("{}".format(rectangle))

        print("\n" * self.y, end="")

        for i in range(self.height):
            rectangle += (" " * self.x) + (print_symbol*self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """ Returns a string format of the rectangle """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Assigns key/value argument to attributes
        kwargs is skipped if args is not empty
        Args:
            *args - variable number of no-keyword args
            **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.w__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """ Returns the dictionary repr of a rect """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
