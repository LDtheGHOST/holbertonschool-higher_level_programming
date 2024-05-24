#!/usr/bin/python3
"""
   Function file for say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """
       Prints "My name is <first name> <last name>".
       Arguments:
           first_name (str): First name to print.
           last_name (str, optional): Second name to print.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
