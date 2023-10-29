#!/usr/bin/python3
"""Module for Matrix Multiplication"""


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices

    Parameters:
        m_a (list of lists): The first matrix to be multiplied.
        m_b (list of lists): The second matrix to be multiplied.

    Raises:
        TypeError: If 'm_a' is not a list or 'm_b' is not a list.
        TypeError: If 'm_a' is not a list of lists or 'm_b' is not a list of
        lists.
        ValueError: If 'm_a' is empty or 'm_b' is empty.
        TypeError: If an element in 'm_a' or 'm_b' is not an integer or a
        float.
        TypeError: If 'm_a' is not a rectangular matrix, i.e., if rows have
        varying sizes.
        TypeError: If 'm_b' is not a rectangular matrix, i.e., if rows have
        varying sizes.
        ValueError: If 'm_a' and 'm_b' cannot be multiplied.

    Returns:
        list of lists: The resulting matrix after the multiplication.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, (list)) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, (list)) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or all(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or all(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    if not all(isinstance(x, (int, float)) for row in m_a for x in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    resultant_matrix = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[0])))
            row.append(element)
        resultant_matrix.append(row)

    return (resultant_matrix)
