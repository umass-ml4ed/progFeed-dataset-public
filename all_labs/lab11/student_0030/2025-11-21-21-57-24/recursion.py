# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def max_recursive(list):
    if len(list) == 0:
        return 0 
    if len(list) == 1:
        return list[0]
    the_rest_max = max_recursive(list[1:])
    if list[0] > the_rest_max:
        return list[0]
    else:
        return the_rest_max
    
def sum_lists_recursive(list1, list2):
    if len(list1) == 0:
        return 0 
    return list1[0] + list2[0] + sum_lists_recursive(list1[1:], list2[1:])

def funky(n):
    if n == 0 or n == 1:
        return 1
    if n % 2 == 0: 
        return 2 * funky(n // 2)
    else:
        return 1 + 2 * funky(n + 1)
