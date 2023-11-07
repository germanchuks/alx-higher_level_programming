#!/usr/bin/python3
"""Script to add all arguments to a Python list, and save to a file"""
import sys


save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from('add_item.json')
except FileNotFoundError:
    my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to(my_list, 'add_item.json')
