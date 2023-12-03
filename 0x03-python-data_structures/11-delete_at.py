#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):  # Check given task conditions
        return my_list
    del my_list[idx]  # Make new_list without idx
    return my_list  # Return new_list without idx
