#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            if x < (len(matrix[i]) - 1):
                print("{:d} ".format(matrix[i][x]), end="")
            else:
                print("{:d}".format(matrix[i][x]), end="")
        if i < (len(matrix[i]) - 1):
            print("")
        else:
            print("", end="")
    print("")
