#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Join all elements in the row as strings with space using str.format
        print(" ".join("{:d}".format(num) for num in row))
