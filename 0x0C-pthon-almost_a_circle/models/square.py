#!/usr/bin/python3
"""Module for Square inheritted from Rectangle"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    This function represents a Square and inherits from the Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
            size (int): The length of a side of the Square.
            x (int, optional): The x-coordinate of the Square (default: 0).
            y (int, optional): The y-coordinate of the Square (default: 0).
            id (int, optional): The ID of the Square (default: None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")

    @property
    def size(self):
        """Gets the size of the square."""
        return (self.width)

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the square by assigning arguments to each attribute.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)
