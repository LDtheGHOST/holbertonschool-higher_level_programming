#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_length = len(sentence)
    if sentence_length == 0:
        new_tuple = (sentence_length, None)
    else:
        new_tuple = (sentence_length, sentence[0])

    return new_tuple