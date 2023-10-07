#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxItem = my_list[0]
    for num in my_list:
        if num > maxItem:
            maxItem = num
    return maxItem
