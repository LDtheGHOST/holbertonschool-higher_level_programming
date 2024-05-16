#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        _size = len(row)
        _i = 0
        for column in row:
            _i += 1
            print(
                    "{:d}".format(column),
                    end="" if _i == _size else " "
                                    
            )
        print()
