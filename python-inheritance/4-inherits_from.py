#!/usr/bin/python3
"""
Shebang to specify the Python 3 interpreter.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a class that inherits from a_class,
              and False if obj is an instance of a_class itself or not related.
    """
    # Check if the object is an instance of a class that inherits from a_class
    # Exclude the case where obj is an instance of a_class itself
    return isinstance(obj, a_class) and type(obj) is not a_class