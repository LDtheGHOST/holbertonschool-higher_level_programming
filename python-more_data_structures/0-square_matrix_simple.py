#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        a = []
        for column in row:
            a.append(column * column)
        new_matrix.append(a)
    return new_matrix
