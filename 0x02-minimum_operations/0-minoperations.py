#!/usr/bin/python3

"""
   write a method that calculates the fewest.
"""


def minOperations(n):
    param_1 = 0
    param_2 = 2
    while n > 1:
        while n % param_2 == 0:
            param_1 += param_2
            n /= param_2
        param_2 += 1
    return param_2
