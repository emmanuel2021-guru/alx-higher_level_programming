#!/usr/bin/python3

"""A module that divides all the elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix

       Args:
            matrix (list of lists): the matrix to be divided
            div (int or float): the divisor
    """
    row_len = len(matrix[0])
    matrix_new = matrix[:]

    for row in matrix:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of\
                        integers/floats")

    for row in matrix:
        if len(row) != row_len:
            print(len(row), row_len)
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row_index in range(len(matrix_new)):
        for col_index in range(len(matrix_new[row_index])):
            matrix_new[row_index][col_index] = round((matrix_new[row_index][col_index] / div), 2)


    return matrix_new
