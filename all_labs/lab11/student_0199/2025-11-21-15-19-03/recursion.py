# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    rest_lst_max = max_recursive(lst[1:])
    if lst[0] > rest_lst_max:
        return lst[0]
    else:
        return rest_lst_max
    
print(max_recursive([3, 10, 2, 8, 6])) # returns 10
print(max_recursive([10, 2, 8, 6]))    # returns 10
print(max_recursive([2, 8, 6]))        # returns 8
print(max_recursive([8, 6]))           # returns 8
print(max_recursive([6]))


