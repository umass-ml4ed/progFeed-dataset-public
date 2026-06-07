# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        lst.remove(min(lst))
        return max_recursive(lst)


def sum_lists_recursive(lst1, lst2):
    if len(lst1) and len(lst2) == 0:
        return 0
    elif len(lst1) and len(lst2) == 1:
        return lst1[0] + lst2[0]
    else:
        end = len(lst1)
        return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:end], lst2[1:end])


def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:
        o = n // 2
        return 2 * funky(o)
    else:
        p = n + 1
        return 1 + 2 * funky(p)