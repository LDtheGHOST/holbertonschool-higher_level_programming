#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    cache = []
    c_set = []
    od_set = []
    for _set in [set_1, set_2]:
        for el in _set:
            if el in cache:
                c_set.append(el)
            else:
                cache.append(el)

    for _set in [set_1, set_2]:
        for el in _set:
            if el not in c_set:
                od_set.append(el)
    return od_set
