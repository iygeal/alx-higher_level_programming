#!/usr/bin/env python3
"""Module to find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - The peak element found in the list.
    """
    if not list_of_integers:
        return None  # If the list is empty, there's no peak

    left = 0  # Initialize the left pointer
    right = len(list_of_integers) - 1  # Initialize the right pointer

    while left < right:
        mid = (left + right) // 2  # Calculate the middle index

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1  # Move the left pointer to the right half
        else:
            right = mid  # Move the right pointer to the left half

    return list_of_integers[left]  # Return the peak element
