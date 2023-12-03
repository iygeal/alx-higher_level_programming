#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    biggest_num = my_list[0]  # Initialize to first member of the list
    for num in my_list:
        if num > biggest_num:  # Check if current number > b_n
            biggest_num = num  # Set biggest_num to current number if true
    return biggest_num  # Now biggest_num is definitely the max

