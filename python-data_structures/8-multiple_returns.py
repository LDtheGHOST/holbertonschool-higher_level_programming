#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        _first = None
    else:
        _first = sentence[0]
    return len(sentence), _first
