#!/usr/bin/python3
"""
Divide matrix function
"""


def matrix_divided(matrix, div):
    """
    Function that divdes a matrix
    """

    errormsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not all(isinstance(row, list)
               and all(isinstance(element, (int, float))
                       for element in row) for row in matrix):
        raise TypeError(errormsg)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result_matrix = [[round(element / div, 2)
                      for element in row] for row in matrix]
    return result_matrix
