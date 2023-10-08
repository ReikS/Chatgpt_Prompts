# -*- coding: utf-8 -*-
"""
Created on Sat May 20 22:35:36 2023

@author: PC
"""

################################################################
# 1st promt
################################################################

def next_dandy(d1):
    # Convert the input to string for easier manipulation
    str_d1 = str(d1)

    # Extract the first and last digit
    first_digit = int(str_d1[0])
    last_digit = int(str_d1[-1])

    # If the last digit is less than 9, just increment the last digit
    if last_digit < 9:
        next_dandy = int(str_d1[:-1] + str(last_digit + 1))

    # If the last digit is 9 and first digit is not 9, increment the first digit and set last digit as first digit + 1
    elif first_digit < 9:
        next_dandy = int(str(first_digit + 1) + str_d1[1:-1] + str(first_digit + 2))

    # If the first digit is 9, the next dandy number will be in the next number of digits
    else:
        next_dandy = int('1' + '0' * len(str_d1) + '2')

    return next_dandy

