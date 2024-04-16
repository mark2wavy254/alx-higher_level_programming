#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element * element)

        new.append(new_row)
    return new
