#!/usr/bin/python3
"""Python script that reads stdin line by line and computes metrics"""

import sys


def print_num(size_of_file, status):
    """outputing total file size and status_t list"""
    print("File size: {:d}".format(size_of_file))
    for key, value in sorted(status_t.items()):
        if value != 0:
            print("{}: {}".format(key, value))


status_t = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}

size_of_file = 0
count = 0
try:
    for line in sys.stdin:
        args = line.split()

        if len(args) > 2:
            status_code = args[-2]
            file_size = int(args[-1])

            if status_code in status_t:
                status_t[status_code] += 1

            size_of_file += file_size
            count += 1

            if count == 10:
                print_num(size_of_file, status_t)
                count = 0

except KeyboardInterrupt:
    pass

finally:
    print_num(size_of_file, status_t)
