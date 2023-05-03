#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """

    :@param n:
    :return:
    """
    if n <= 1:
        return 0
    for x in range(2, n+1):
        if n % x == 0:
            return minOperations(int(n/x)) + x
