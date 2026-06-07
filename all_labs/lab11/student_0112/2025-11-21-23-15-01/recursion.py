# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def max_recursive(lst):
    if (len(lst) == 0):
        return 0
    elif (len(lst) == 1):
        return lst[0]
    else:
        return max(lst[0], max_recursive(lst[1:]))
# print(max_recursive([3, 10, 2, 8, 6]))
def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:],lst2[1:])
def funky(n):
    if n == 1 or n ==0:
        return 1
    elif (n%2 == 0):
        return funky(n//2)
    else:
        return 1+2*funky(n+1)
    