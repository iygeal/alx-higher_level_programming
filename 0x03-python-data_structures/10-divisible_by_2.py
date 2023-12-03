#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []  # Create an empty list
    for i in my_list:  # Iterate through the original list
        new_list.append(i % 2 == 0)  # Append the check for i % 2 to new_list
    return new_list  # Return new_list, which now tells if i % 2 = 0
