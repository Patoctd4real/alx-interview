#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""

import sys


def printing_metric(e_file_size, log_status):
    """getting the total file size and status list"""
    print("File size: {:d}".format(e_file_size))
    for key, value in sorted(log_status.items()):
        if value != 0:
            print("{}: {}".format(key, value))


log_status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}

e_file_size = 0
count = 0
try:
    for line in sys.stdin:
        args = line.split()

        if len(args) > 2:
            codes_status = args[-2]
            file_size = int(args[-1])

            if codes_status in log_status:
                log_status[codes_status] += 1

            e_file_size += file_size
            count += 1

            if count == 10:
                printing_metric(e_file_size, log_status)
                count = 0

except KeyboardInterrupt:
    pass

finally:
    printing_metric(e_file_size, log_status)
