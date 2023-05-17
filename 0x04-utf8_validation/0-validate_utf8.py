#!/usr/bin/python3
"""
Method that determines if a given data set represents a valid UTF-8 encoding.
* Return: True if data is a valid UTF-8 encoding, else return False
* A character in UTF-8 can be 1 to 4 bytes long
* The data set can contain multiple characters
* The data will be represented by a list of integers
* Each integer represents 1 byte of data, therefore you only need
* to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """ UTF-8 Validation """
    byteLenght = 0
    byteMovement = 1 << 7
    byteMovement1 = 1 << 6
    for byte in data:
        byteMove = 1 << 7
        if byteLenght == 0:
            while byte & byteMove:
                byteLenght += 1
                byteMove = byteMove >> 1
            if byteLenght == 0:
                continue
            if byteLenght == 1 or byteLenght > 4:
                return False
        else:
            if not (byte & byteMovement and not (byte & byteMovement1)):
                return False
        byteLenght -= 1
    if byteLenght == 0:
        return True
    return False
