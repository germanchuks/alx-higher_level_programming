#!/usr/bin/python3
def uniq_add(my_list=[]):
    uList = [item for i, item in enumerate(my_list) if item not in my_list[:i]]
    return sum(unique_list)
