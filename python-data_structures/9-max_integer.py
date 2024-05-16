#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    _check = None
    for _int in my_list:
        if _check is None or _int > _check:
            _check = _int
    return _check
