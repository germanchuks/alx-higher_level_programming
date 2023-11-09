#!/usr/bin/python3
"""Module for Rectangle inheritted from Base"""
from base import Base


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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle."""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the rectangle."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle."""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the rectangle."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def display(self):
        """
        Displays the rectangle using '#' characters.
        """
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            for _ in range(self.__x):
                print(' ', end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Updates the rectangle by assigning arguments to each attribute.
        """
        attributes = ["id", "width", "height", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)
