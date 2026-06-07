# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if len(lst)==0:
        return 0
    if len(lst)==1:
        return lst[0]
    prev= max_recursive(lst[1:])
    if lst[0] > prev:
        return lst[0]
    else:
        return prev


def sum_lists_recursive(lst1, lst2):
