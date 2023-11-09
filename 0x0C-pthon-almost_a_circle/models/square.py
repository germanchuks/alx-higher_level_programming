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
        Returns a string representation of the rectangle.
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")
