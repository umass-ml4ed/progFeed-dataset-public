# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    if lst[0] >= lst[1]:
        lst.pop(1)
    else:
        lst.pop(0)
    return max_recursive(lst)

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    if len(lst1) == 1:
        return lst1[0] + lst2[0]
    count = lst1[0] + lst2[0]
    lst1.pop(0)
    lst2.pop(0)
    return count + sum_lists_recursive(lst1, lst2)

def funky(num):
    if num == 0 or num == 1:
        return 1
    elif num % 2 == 0:
        return 2 * funky(num // 2)
    else:
        return 1 + 2 * funky(num + 1)