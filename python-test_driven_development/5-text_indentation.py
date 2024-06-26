#!/usr/bin/python3
"""
    Function file for text_indentation.
"""


def text_indentation(text):
    """
       Prints a text with 2 new lines after each characters
       `.`, `?`, `:`
       Arguments:
           text (str): Text to formated.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d
            
    print(s[:-3], end="")
