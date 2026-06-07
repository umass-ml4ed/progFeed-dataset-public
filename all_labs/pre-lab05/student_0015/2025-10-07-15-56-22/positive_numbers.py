# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED



# positive_numbers.py

def filter_positive(numbers):
    """
    Takes a list of integers and returns a new list 
    containing only the positive numbers (> 0).

    Must use a for loop (no list comprehensions).
    """
    positives = []  # create an empty list to store positive numbers

    for n in numbers:  # loop through each element
        if n > 0:
            positives.append(n)  # add positive number to the list

    return positives  # return the new list