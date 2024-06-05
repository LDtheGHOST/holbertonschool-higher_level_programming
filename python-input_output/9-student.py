#!/usr/bin/python3
"""
    File class for Student.
"""


class Student:
    """ Class of a student. """

    def __init__(self, first_name, last_name, age):
        """
            Initialization of a student.
            Arguments:
                first_name (str): First name of the student.
                last_name (str): Last name of the student.
                age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Get the json format of the Student class.
        """
        return self.__dict__
