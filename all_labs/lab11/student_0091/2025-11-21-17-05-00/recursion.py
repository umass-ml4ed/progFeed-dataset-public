# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0

    if len(lst) == 1:
        return lst[0]

    first = lst[0]
    max_rest = max_recursive(lst[1:])

    if first > max_rest:
        return first
    else:
        return max_rest


def sum_lists_recursive(lst1, lst2):
    #base case
    if len(lst1) == 0 and len(lst2) == 0:
        return 0

    else:
        # first sum
        first_sum=lst1[0]+lst2[0]
        #progression
        rest_of_lst=sum_lists_recursive(lst1[1:], lst2[1:])
        return first_sum + rest_of_lst      #first sum, call new smaller list, first sum1 + first sum2, call new smaller list, repeat


print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))












