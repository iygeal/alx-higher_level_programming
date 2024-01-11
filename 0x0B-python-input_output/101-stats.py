#!/usr/bin/python3
"""
Script to read stdin line by line and compute metrics
"""


def print_stats(size, status_codes):
    """Print accumulated metrics
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    # Initialize metrics variables
    size = 0
    status_codes = {'200': 0, '301': 0, '400': 0,
                    '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    count = 0

    def update_metrics(line, size, status_codes):
        """Update metrics based on the input line
        """
        try:
            size += int(line[-1])
        except (IndexError, ValueError):
            pass

        try:
            if line[-2] in status_codes:
                status_codes[line[-2]] += 1
        except IndexError:
            pass

        return size, status_codes

    try:
        for line in sys.stdin:
            # Print statistics every 10 lines
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            # Split the input line into parts
            line = line.split()

            # Update metrics based on the line
            size, status_codes = update_metrics(line, size, status_codes)

        # Print final statistics
        print_stats(size, status_codes)

    except KeyboardInterrupt:
        # Handle keyboard interruption (Ctrl+C)
        print_stats(size, status_codes)
        raise
