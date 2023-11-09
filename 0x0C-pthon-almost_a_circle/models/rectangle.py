#!/usr/bin/python3
"""Module for Rectangle inheritted from Base"""
Base = __import__('base').Base


class Rectangle(Base):
    """
    This function represents a rectangle and inherits from the Base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle (default: 0).
            y (int, optional): The y-coordinate of the rectangle (default: 0).
            id (int, optional): The ID of the rectangle (default: None).
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """Gets the width of the rectangle."""
            return (self.__width)

        @width.setter
        def width(self, value):
            """Sets the width of the rectangle."""
            self.__width = value

        @property
        def height(self):
            """Gets the height of the rectangle."""
            return (self.__height)

        @height.setter
        def height(self, value):
            """Sets the height of the rectangle."""
            self.__height = value

        @property
        def x(self):
            """Gets the x-coordinate of the rectangle."""
            return (self.__x)

        @x.setter
        def x(self, value):
            """Sets the x-coordinate of the rectangle."""
            self.__x = value

        @property
        def y(self):
            """Gets the y-coordinate of the rectangle."""
            return (self.__y)

        @y.setter
        def y(self, value):
            """Sets the y-coordinate of the rectangle."""
            self.__y = value

