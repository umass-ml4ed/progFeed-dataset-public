# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    if lst[0] < lst[1]:
        return max_recursive(lst[1:])
    else:
        return max_recursive([lst[0]] + lst[2:])

def sum_lists_recursive(lst1, lst2, x = 0):
        if len(lst1) and len(lst2) == 0:
                return x
        x = x + lst1.pop(0) + lst2.pop(0)
        return sum_lists_recursive(lst1, lst2, x)

def funky(n):
    if n == 0 or n == 1:
        return 1
    if n % 2 == 0:
        return 2 * funky(n // 2)
    return 1 + 2 * funky(n + 1)

        