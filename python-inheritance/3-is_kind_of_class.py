#!/usr/bin/python3
"""
Shebang to specify the Python 3 interpreter.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of a_class,
              False otherwise.
    """
    # Use isinstance to check both direct and inherited class relationships
    return isinstance(obj, a_class)