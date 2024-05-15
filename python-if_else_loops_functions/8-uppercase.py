#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        _c = str[i]
        _result = ord(_c)
        if _result >= 97 and _result <= 122:
            _c = chr(_result - 32)
            print("{:s}".format(_c), end="")
            print("")
