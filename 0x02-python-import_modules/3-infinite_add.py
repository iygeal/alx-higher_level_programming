#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total_args = 0
    argc = len(argv)
    for i in range(1, argc):
        total_args += int(argv[i])
    print(total_args)
