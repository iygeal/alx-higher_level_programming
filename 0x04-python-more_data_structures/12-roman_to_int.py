#!/usr/bin/python3
def roman_to_int(roman_string):
    # If the input is None or not a string, return 0
    if not roman_string or type(roman_string) is not str:
        return 0
    # Initialize int_total to 0
    int_total = 0
    # Create a dictionary mapping Roman numerals to integers
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    # Iterate over the string in reverse order
    for roman in reversed(roman_string):
        # Get the integer value of the current Roman numeral
        arabic_num = digits[roman]
        # Add or subtract the value based on the comparison
        # of the current value and the int_total
        int_total += arabic_num if int_total < arabic_num * 5 else -arabic_num
    # Return the int_total integer value
    return int_total
