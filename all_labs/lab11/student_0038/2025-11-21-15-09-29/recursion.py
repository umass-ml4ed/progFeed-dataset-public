# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    length = len(lst)
    if length == 0:
        return 0
    else:
        return max(lst[0], max_recursive(lst[1:]))

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0 or len(lst2) == 0:
        return 0
    else:
        return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])
print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) # returns 21
print(sum_lists_recursive([2, 3], [5, 6]))       # returns 16
print(sum_lists_recursive([3], [6]))             # returns 9
print(sum_lists_recursive([],[])) 

# def funky()

