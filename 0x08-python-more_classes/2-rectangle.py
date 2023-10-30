#!/usr/bin/python3
"""Module for a Rectangle"""


class Rectangle:
    """
    This class represents a rectangle.

    A rectangle is a geometric shape with two sides of different lengths,
    forming four right angles.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width=0, height=0): Initializes a new Rectangle
        instance with the given width and height.

    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle. It must be a positive
            integer value.
            height (int): The height of the rectangle. It must be a positive
            integer value.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle. It must be a positive
            integer value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle. It must be a positive
            integer value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Compute and return the area of the rectangle.

        Returns:
            int: The area of the rectangle (product of its width and height)
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Compute and return the perimeter of the rectangle
        (the sum of all four sides).

        Returns:
            int: The perimeter of the rectangle.
            If either the width or height is 0, the perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2*(self.__width + self.__height)
        return (perimeter)
