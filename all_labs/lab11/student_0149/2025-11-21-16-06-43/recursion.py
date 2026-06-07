# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max = max_recursive(lst[1:])
        first_item = lst[0]
        if first_item < max:
            return max
        if first_item >= max:
            return first_item
            


def sum_lists_recursive(list1,list2):
    if len(list1) == 0:
        return 0
    sum_count = 0 
    sum_count+= list1[0] + list2[0]
    sum_count+= sum_lists_recursive(list1[1:],list2[1:])
    return sum_count

def funky(n):
    if n == 0 or n == 1:
        return 1
    if n%2 == 0:
        return (2*funky(n//2))
    else:
        return (1+2*(funky(n+1)))

    
