# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lis):
    if len(lis) < 1:
        return 0
    elif len(lis) == 1:
        return lis[0]
    else:
        sub_max = max_recursive(lis[1:])
        if lis[0] > sub_max:
            return lis[0]
        else:
            return sub_max

def sum_lists_recursive(lst1, lst2):
    if (len(lst1) or len(lst2)) == 0:
        return 0
    else:
        ad = lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])
        return ad

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n%2 == 0:
        new1 = 2*funky(n//2)
        return new1
    else:
        new2 = 1 + 2*funky(n+1)
        return new2




