#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_x = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            print_x = print_x + 1
    except IndexError:
        pass
    finally:
        print()
    return (print_x)
