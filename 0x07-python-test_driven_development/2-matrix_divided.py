#!/usr/bin/python3
"""Module for dividing all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by an integer or float

    This function takes two arguments, a matrix and a non-zero int or float.
    It returns a new matrix containing elements from input matrix divided by
    the number 'div', rounded to two decimal places.

    Parameters:
        matrix (list of lists): The matrix to be divided.
        div (int or float): Number to divide the matrix by.

    Returns:
        list of lists:  The matrix divided by number 'div'.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not of type integer or float.
        ZeroDivisionError: If div is equal to zero.
    """
    if not isinstance(matrix, (list)) or (
       not all(isinstance(row, (list)) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix(list of lists) of integers/floats")

    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError(
            "matrix must be a matrix(list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x/div, 2) for x in row] for row in matrix]
