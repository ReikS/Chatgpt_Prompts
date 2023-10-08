# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def is_dank(i):
    """
    This function checks whether a given integer is a "dank" number.
    A "dank" number is defined as a number where the first and last digits are the same and non-zero.

    :param i: The integer to check.
    :return: True if the number is "dank", False otherwise.
    """
    
    # Check if the number is a positive integer
    if not isinstance(i, int) or i <= 0:
        return False

    # Convert the integer to a string to easily access the first and last digits
    str_i = str(i)

    # Get the first and last characters of the string
    first_char = str_i[0]
    last_char = str_i[-1]

    # Check if the first and last characters are the same and not '0'
    if first_char == last_char and first_char != '0':
        return True
    else:
        return False


def next_dank_0(d1):
    """
    This function generates the next "dank" number that is strictly larger than the given number.

    :param d1: The "dank" number to start from.
    :return: The next "dank" number larger than d1.
    """
    
    # Check if the input number is dank
    if not is_dank(d1):
        raise ValueError("Input number is not dank")

    # Start from the number after d1
    d2 = d1 + 1

    # Keep incrementing d2 until we find a dank number
    while not is_dank(d2):
        d2 += 1

    # Return the found dank number
    return d2


def next_dank_1(d1):
    """
    Wrong result, gives 551 for d1 = 55.
    This function generates a "dank" number that is strictly larger than the given number.

    :param d1: The "dank" number to start from.
    :return: A "dank" number larger than d1.
    """
    
    # Check if the input number is dank
    if not is_dank(d1):
        raise ValueError("Input number is not dank")

    # Convert the dank number to a string
    str_d1 = str(d1)
    
    # Get the first digit of d1
    first_digit = str_d1[0]
    
    # Create a new dank number by adding '1' to the end of the string representation of d1, 
    # and replacing the first character with the first digit of d1 to ensure it's the same as the last digit
    d2 = int(first_digit + str_d1[1:] + '1')

    return d2


def next_dank_2(d1):
    """
    Second try, gives wrong result for 959.
    This function generates a "dank" number that is strictly larger than the given number.

    :param d1: The "dank" number to start from.
    :return: A "dank" number larger than d1.
    """
    
    # Check if the input number is dank
    if not is_dank(d1):
        raise ValueError("Input number is not dank")

    # Convert the dank number to a string
    str_d1 = str(d1)
    
    # Get the first digit of d1 and increment it, unless it's 9, in which case leave it as is
    first_digit = int(str_d1[0])
    first_digit = min(first_digit + 1, 9)
    
    # Get the length of the middle section (all digits except the first and last)
    middle_length = len(str_d1) - 2

    # Construct the next dank number
    d2 = int(str(first_digit) + '0' * middle_length + str(first_digit))

    return d2


def next_dank_3(d1):
    """
    This function generates a "dank" number that is strictly larger than the given number.

    :param d1: The "dank" number to start from.
    :return: A "dank" number larger than d1.
    """
    
    # Check if the input number is dank
    if not is_dank(d1):
        raise ValueError("Input number is not dank")

    # Convert the dank number to a string
    str_d1 = str(d1)
    
    # Get the first digit of d1
    first_digit = int(str_d1[0])
    
    if first_digit < 9:
        # If the first digit is less than 9, increment it
        first_digit += 1
        # Get the length of the middle section (all digits except the first and last)
        middle_length = len(str_d1) - 2
        # Construct the next dank number
        d2 = int(str(first_digit) + '0' * middle_length + str(first_digit))
    else:
        # If the first digit is 9, increase the number of digits by 1 and set the first and last digits to 1
        d2 = int('1' + '0' * len(str_d1) + '1')

    return d2


def next_dank_4(d1):
    """
    Incorrect, since next_dank_4(4) gives 55.
    This function generates the next "dank" number that is strictly larger than the given number.

    :param d1: The "dank" number to start from.
    :return: The next "dank" number larger than d1.
    """
    
    # Check if the input number is dank
    if not is_dank(d1):
        raise ValueError("Input number is not dank")

    # Convert the dank number to a string
    str_d1 = str(d1)
    
    # Get the first digit of d1
    first_digit = int(str_d1[0])

    # If the last digit is less than the first digit, simply increment the last digit to get the next dank number
    if int(str_d1[-1]) < first_digit:
        d2 = int(str_d1[:-1] + str(first_digit))
    else:
        # Check if all middle digits are 9
        if all(d == '9' for d in str_d1[1:-1]):
            # Increment the first digit and reset all middle digits to 0
            d2 = int(str(first_digit + 1) + '0' * (len(str_d1) - 2) + str(first_digit + 1))
        else:
            # Add 10 to the power of the number of trailing digits that are equal to the first digit
            num_trailing_digits = len(str_d1) - str_d1.rfind(str(first_digit))
            d2 = d1 + 10 ** num_trailing_digits

    return d2


def next_dank_5(d1):
    """
    This function generates the next "dank" number that is strictly larger than the given number.

    :param d1: The "dank" number to start from.
    :return: The next "dank" number larger than d1.
    """
    
    # Check if the input number is dank
    if not is_dank(d1):
        raise ValueError("Input number is not dank")

    # Convert the dank number to a string
    str_d1 = str(d1)
    
    # Get the first digit of d1
    first_digit = int(str_d1[0])

    # If the number is a single digit from 1 to 8
    if d1 < 9:
        return d1 + 1

    # If the number is 9
    elif d1 == 9:
        return 11

    # If the number is a two-digit dank number
    elif len(str_d1) == 2:
        if d1 == 99:
            return 101
        else:
            return d1 + 11

    # If the number has three or more digits and all digits in the middle are 9
    elif all(d == '9' for d in str_d1[1:-1]):
        return int(str(first_digit + 1) + '0' * (len(str_d1) - 2) + str(first_digit + 1))

    # For all other dank numbers with three or more digits
    else:
        num_trailing_digits = len(str_d1) - str_d1.rfind(str(first_digit))
        return d1 + 10 ** num_trailing_digits

