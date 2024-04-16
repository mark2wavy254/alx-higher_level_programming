#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sd = sorted(a_dictionary.keys())
    for key in sd:
        print(f"{key}: {a_dictionary[key]}")
