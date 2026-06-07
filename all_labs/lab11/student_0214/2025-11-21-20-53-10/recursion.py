# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    if lst[0] > lst[1]:
        lst.pop(1)
    else:
        lst.pop(0)
    return max_recursive(lst)

def sum_lists_recursive(lst1,lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return 0
    if len(lst1) == 1 and len(lst2) == 1:
        return lst1[0] + lst2[0]
    item1 = lst1[0] + lst1[1]
    item2 = lst2[0] + lst2[1]
    new_lst1 = []
    new_lst2 = []
    new_lst1.append(item1)
    new_lst2.append(item2)
    new_lst1[1:] = lst1[2:]
    new_lst2[1:] = lst2[2:]
    return sum_lists_recursive(new_lst1, new_lst2)

def funky(n):
    if n == 1 or n == 0:
        return 1
    if n % 2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n + 1)
