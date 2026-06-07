# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = max_recursive(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest
    
print(max_recursive([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))



def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return []
    else:
        first_sum = lst1[0] + lst2[0]
        rest_sum = sum_lists_recursive(lst1[1:], lst2[1:])
        return [first_sum] + rest_sum
    
print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))
