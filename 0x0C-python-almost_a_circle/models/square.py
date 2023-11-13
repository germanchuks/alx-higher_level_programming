#!/usr/bin/python3
"""Module for Square inheritted from Rectangle"""
from models.rectangle import Rectangle
from models.base import Base


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
        attributes = ["id", "size", "x", "y"]

        if args:
            for i in range(len(args)):
                if args[i] is None and attributes[i] == "id":
                    Base._Base__nb_objects += 1
                    setattr(self, attributes[i], Base._Base__nb_objects)
                else:
                    setattr(self, attributes[i], args[i])
        else:
            if "id" in kwargs and kwargs["id"] is None:
                Base._Base__nb_objects += 1
                kwargs["id"] = Base._Base__nb_objects

            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the square.
        """
        custom_dict = {'id': self.id, 'x': self.x, 'size': self.width,
                       'y': self.y}
        return (custom_dict)
