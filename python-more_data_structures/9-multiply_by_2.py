#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_diction = a_dictionary.copy()
    diction_keys = list(new_diction.keys())

    for i in diction_keys:
        new_diction[i] *= 2

    return new_diction