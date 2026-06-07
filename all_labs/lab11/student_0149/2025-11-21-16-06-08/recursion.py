# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        first_item = lst[0]
        rest = max_recursive(lst[1:])
        if first_item <= max(rest):
            return first_item


def sum_lists_recursive(list1,list2):
    if len(list1) == 0:
        return 0
    
max_recursive([3, 10, 2, 8, 6])