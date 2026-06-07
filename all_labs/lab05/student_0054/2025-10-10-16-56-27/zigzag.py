# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED


"""Write a function, called is_zigzag, 
inside the file zigzag.py, which should:
(1)Take a list of integers as a parameter
(2)Return True if the list follows a zigzag pattern,
and False otherwise.(3)A list with fewer than 3 elements 
should return True (since there is no middle element to
violate the rule)"""

# zigzag is if every element (except the first and last) is either
# strictly greater than both its neighbors or strictly smaller (~)
def is_zigzag (_list):
    if len(_list) < 3:
        return True
    for i in range(1, len(_list) - 1): 
        if not ((_list[i] > _list[i - 1] and _list[i] > _list[i + 1]) or (_list[i] < _list[i - 1] and _list[i] < _list[i + 1])):
            return False
    return True
    