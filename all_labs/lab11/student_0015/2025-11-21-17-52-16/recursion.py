# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED


def max_recursive(lst):
    #list empty and if len of list one then index 0 p
    if lst == []:
        return 0
    if len(lst) == 1:
        return lst[0]
    rest_max = max_recursive(lst[1:])
    if lst[0] > rest_max: #now compare to find greatest no.
        return lst[0]
    else:
        return rest_max

def sum_lists_recursive(lst1, lst2):
    if lst1 == [] and lst2 == []:
        return 0
    first_sum = lst1[0] + lst2[0]
    return first_sum + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if abs(n) < 2:
        return n
    return funky(n - 2) + 4*n
