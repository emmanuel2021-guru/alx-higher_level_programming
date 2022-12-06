#!/usr/bin/python
def print_matrix_integer(matrix=[[]]):
    """A function that prints a matrix of integers"""
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            print("{:d}".format(matrix[row][column]), end=" ")
        print("")
