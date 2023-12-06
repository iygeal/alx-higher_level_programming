#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({str(key): value})  # Another way is
    return a_dictionary                     # a_dictionary = value
