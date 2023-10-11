#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or not my_list:
        return 0
    num = 0
    divisor = 0
    for score, weight in my_list:
        num += score * weight
        divisor += weight
    return num / divisor
