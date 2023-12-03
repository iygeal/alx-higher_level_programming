#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):  # Check given task conditions
        return my_list
    new_list = my_list[:idx] + my_list[idx+1:]  # Make new_list without idx
    return new_list  # Return new_list without idx
