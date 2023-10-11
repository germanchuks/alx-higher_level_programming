#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = 0
    dict_list = list(a_dictionary.items())
    for i in dict_list:
        if i[1] > max:
            max = i[1]
            maxName = i[0]
    return maxName
