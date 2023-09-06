#!/usr/bin/python3
"""
lazy_matrix module
calculates multiplication of matrix using numpy lib

"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """Return: matrix of the product of m_a and m_b
    Args:
    param1: list m_a
    param2: list m_b
    Raise: TypeError, ValueError
    """
    return (numpy.matmul(m_a, m_b))
