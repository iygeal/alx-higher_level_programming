#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []  # Create new list
    for element in my_list:  # Iterate through original list
        if element == search:  # Check for occurence of search element
            new_list.append(replace)  # Replace in newlist if found
        else:
            new_list.append(element)  # Return original if not found
    return new_list  # Return the newly modified (or not) list
