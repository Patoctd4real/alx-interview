#!/usr/bin/python3

"""
   there is a single character H. Your text editor
   can execute only two operations in this file: Copy All and Paste.
   Given a number n, write a method that calculates the fewest
   number of operations needed to result in
   exactly n H characters in the file.
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
