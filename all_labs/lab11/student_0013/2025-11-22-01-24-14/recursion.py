# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def max_recursive(lst):
    
    if len(lst) == 1:
        return lst[0]
    
    rest_max = max_recursive(lst[1:])
    
    if lst[0] > rest_max :
        return lst[0]
    else:
        return rest_max




print(max_recursive([3, 10, 6, 22, 1]))  
print(max_recursive([66, 2, 3, 52,7]))  


def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

print(sum_lists_recursive((1,2,3,4,5),(6,7,8,9,10)))
