#!/usr/bin/python3
def roman_to_int(roman_string):
    if not str(roman_string) or not roman_string:
        return 0
    roman_styles = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                    'D': 500, 'M': 1000}
    roman_num = 0
    prev_value = 0

    for i in reversed(roman_string):
        if i in roman_styles:
            if roman_styles[i] >= prev_value:
                roman_num += roman_styles[i]
            else:
                roman_num -= roman_styles[i]
            prev_value = roman_styles[i]

    return roman_num
