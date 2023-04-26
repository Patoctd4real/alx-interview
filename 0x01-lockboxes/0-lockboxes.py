#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""


def canUnlockAll(boxes):
    """Determines if boxes can be unlocked"""
    station = 0
    unlockedBoxes = {}

    for box in boxes:
        if len(box) == 0 or station == 0:
            unlockedBoxes[station] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != station:
                unlockedBoxes[key] = key
        if len(unlockedBoxes) == len(boxes):
            return True
        station += 1
    return False
