# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def max_recursive(lst):
    if type(lst) != list:
        return int(lst)
    else:
        sort = sorted(lst)
        num = sort.pop(-1)
        return max_recursive(num)

def sum_lists_recursive(lst1, lst2):
    if len(lst1) > 0 and len(lst2) > 0:
        l1 = lst1.pop(0)
        l2 = lst2.pop(0)
        total = l1 + l2
        return total + sum_lists_recursive(lst1, lst2)
    else:
        return 0

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n%2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n+1)

