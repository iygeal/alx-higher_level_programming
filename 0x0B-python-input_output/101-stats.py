#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics"""

import sys
import signal
from collections import defaultdict

# Initialize variables for metrics
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0


def print_statistics():
    """
    Print statistics based on the accumulated metrics.
    """
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_code_counts):
        print("{}: {}".format(status_code, status_code_counts[status_code]))

# Set up a signal handler for SIGINT (Ctrl+C)


def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1

        # Parse the line
        parts = line.split()
        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update metrics
            total_file_size += file_size
            status_code_counts[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle keyboard interruption (Ctrl+C)
    print_statistics()
    sys.exit(0)
