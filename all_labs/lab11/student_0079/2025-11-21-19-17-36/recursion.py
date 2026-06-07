# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(list):
    if len(list) == 0:
        return 0
    if len(list) == 1:
        return list[0]
    submax = max_recursive(list[1:])
    if list[0] > submax:
        return list[0]
    else:
        return submax

def sum_lists_recursive(list1, list2):
    if len(list1) == 0:
        return 0
    return list1[0] + list2[0] + sum_lists_recursive(list1[1:], list2[1:])

def funky(n):
    if abs(n) <= 2:
        return n
    if n > 2:
        return abs(n) + funky(n - 2)
    else:
        return abs(n) + funky(n + 2)