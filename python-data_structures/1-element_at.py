#!/usr/bin/python3
def element_at(my_list, idx):
    if my_list:
        if idx < 0:
            return
        elif idx > len(my_list) - 1:
            return
        else:
            return my_list[idx]