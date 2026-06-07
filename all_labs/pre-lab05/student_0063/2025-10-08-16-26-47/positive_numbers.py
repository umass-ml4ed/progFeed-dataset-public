# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

'''Write a function, called filter_positive, inside positive_numbers.py, which should:
Take a list of integers as a parameter
Use a for loop to check each element in the list
Collect only the positive numbers (greater than 0) into a new list
Return the new list
Important notes:
You must use a for loop to build the list.
You may not use list comprehensions for this problem.
The return type of your function must be a list of integers.
If there are no positive numbers, return an empty list [].'''

def filter_positive(lis):
    pos = []
    for x in lis:
        if x > 0:
            pos.append(x)
    return pos
        
print(filter_positive([1, -3, 5, 0, -2, 7]))
# [1, 5, 7]

print(filter_positive([-5, -1, -10]))
# []

print(filter_positive([10, 20, -30, 40]))
# [10, 20, 40]

'''def filter_positive(lis):
    positives = []
    for x in lis:
        if x > 0:
            positives.append(x)
    return positives
'''
