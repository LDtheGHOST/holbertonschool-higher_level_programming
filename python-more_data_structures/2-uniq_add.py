#!/usr/bin/python3
def uniq_add(my_list=[]):
    cache = []
    result = 0
    for el in my_list:
        if el in cache:
            continue
        cache.append(el)
        result += el
    return result
