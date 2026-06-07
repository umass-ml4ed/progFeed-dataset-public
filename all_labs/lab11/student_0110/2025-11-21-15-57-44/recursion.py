# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        sort = sorted(lst)
        sort.pop(0)
        return max_recursive(sort)

def sum_lists_recursive(lst1, lst2):
    if len(lst1) > 0 and len(lst2) > 0:
        t1 = lst1.pop(0)
        t2 = lst2.pop(0)
        total = t1 + t2
        return total + sum_lists_recursive(lst1, lst2)
    else:
        return 0

#print(sum_lists_recursive([],[]))

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n%2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n+1)

