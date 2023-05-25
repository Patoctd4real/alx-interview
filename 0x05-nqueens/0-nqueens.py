#!/usr/bin/python3
"""
N queens
"""

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_que = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_que < 4:
    print('N must be at least 4')
    exit(1)


def solving_nque(n):
    '''self descriptive'''
    if n == 0:
        return [[]]
    inner_solution = solving_nque(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_que)
            for solution in inner_solution
            if saf_que((n, i + 1), solution)]


def attacking_que(square, queen):
    '''self descriptive'''
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def saf_que(sqr, queens):
    '''self descriptive'''
    for queen in queens:
        if attacking_que(sqr, queen):
            return False
    return True


for answer in reversed(solving_nque(n_que)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)
