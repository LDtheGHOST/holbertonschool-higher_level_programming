#!/usr/bin/python3
"""
    Function file for add_integer.
"""


def add_integer(a, b=98):
    """
        Adds 2 integers.
        Arguments:
            a (int): Number 1
            b (int, optional): Number 2
        Return:
            (int): Resultat of addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
