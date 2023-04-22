#!/usr/bin/python3
"""
    0-pascal_triangle.py: pascal_triangle()
"""
def pascal_triangle(n):
    """
    Returns the first n rows of Pascal's triangle.
    """
    if n <= 0:
        return []

    answer = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = answer[-1][j-1] + answer[-1][j]
        answer.append(row)

    return answer
