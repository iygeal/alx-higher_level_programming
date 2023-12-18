#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_x = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            print_x += 1
        except (IndexError, ValueError, TypeError):
            pass
    print()
    return (print_x)