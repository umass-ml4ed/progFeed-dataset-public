# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    index = 0
    if (len(lst) == 1):
        return lst[index]
    if ((len(lst) == 0)):
        return 0
    if (lst[index] < lst[index + 1]):
        lst.pop(index)
        return max_recursive(lst)
    else: 
        lst.pop(index + 1)
        return max_recursive(lst)
    

def sum_lists_recursive(lst1, lst2):
    sum = 0
    if (len(lst1) == 0 and len(lst2) == 0):
        return sum
    sum = lst1[0] + lst2[0]
    lst1 = lst1[1:] 
    lst2 = lst2[1:]
    return sum + sum_lists_recursive(lst1, lst2)


def funky(n):
    if (n == 0 or n == 1):
        return 1
    if (n % 2 == 0):
        return 2 * funky(n // 2)
    else:
        return 1 + 2 * funky(n + 1)
