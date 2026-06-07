# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    if len(lst) >= 2:
        if lst[0] >= lst[1]:
            lst.pop(1)
            return max_recursive(lst)
        elif lst[0] < lst[1]:
            lst.pop(0)
            return max_recursive(lst)

def sum_lists_recursive(lst1, lst2):
    if type(lst1) == int:
        if len(lst2) != 0:
            lst1 += lst2.pop(0)
            return sum_lists_recursive(lst1, lst2)
        else:
            return lst1
    elif len(lst1) == 0 and len (lst2) == 0:
        return 0
    elif len(lst1) != 0:
        lst2.append(lst1.pop(0))
        if len(lst1) == 0:
            lst1 = 0
        return sum_lists_recursive(lst1, lst2)

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n%2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n + 1)
