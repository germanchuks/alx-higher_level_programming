#!/usr/bin/python3
"""Module for Lazy Matrix Multiplication"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices by using the module NumPy.

    Parameters:
        m_a (list of lists): The first matrix to be multiplied.
        m_b (list of lists): The second matrix to be multiplied.

    Returns:
        list of lists: The resulting matrix after the multiplication.
    """
    result = np.matmul(m_a, m_b)

    return (result)
