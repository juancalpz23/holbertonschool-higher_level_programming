#!/bin/usr/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        row = [value ** 2 for value in i]
        new_matrix.append(row)
    return new_matrix
