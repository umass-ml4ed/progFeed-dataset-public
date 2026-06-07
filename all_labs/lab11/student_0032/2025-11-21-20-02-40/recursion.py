# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def max_recursive(lst): 
    if not lst:
        return 0 
    if len(lst) == 1:
        return list[0]
    else: 
        maximum_for_rest_of_list = max_recursive(lst[1:])
        return lst[0] if lst[0]>maximum_for_rest_of_list else maximum_for_rest_of_list
    
def sum_lists_recursive(lst1, lst2):
    the_sum += lst1[0] + lst2[0]

    if len(lst1) == 1:
        return the_sum
    else: 
        sum_lists_recursive(lst1[1:], lst2[1:])
        