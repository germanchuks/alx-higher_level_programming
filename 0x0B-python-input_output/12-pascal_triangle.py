#!/usr/bin/python3
"""Function to return pascal's triangle"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers reresenting the pascal's
    triangle of n.

    Args:
    n (int): The number of rows to generate in pascal's triangle.

    Returns:
    list of lists: A list of lists of the pascal's triangle, if n > 0,
    otherwise returns an empty list.
    """
    if n <= 0:
        return []

    pascals_triangle = []

    for i in range(n):
        if i == 0:
            row = [1]
        else:
            previous_row = pascals_triangle[i - 1]
            row = [1]
            for j in range(1, i):
                row.append(previous_row[j - 1] + previous_row[j])
            row.append(1)

        pascals_triangle.append(row)

    return (pascals_triangle)
