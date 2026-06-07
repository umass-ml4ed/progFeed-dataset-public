# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if lst[0] == max(lst):
        return lst[0]
    return max_recursive(lst[1:])

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    summy = lst1[0] + lst2[0]
    lst1.pop(0)
    lst2.pop(0)
    return summy + sum_lists_recursive(lst1, lst2)

print(sum_lists_recursive([], []))