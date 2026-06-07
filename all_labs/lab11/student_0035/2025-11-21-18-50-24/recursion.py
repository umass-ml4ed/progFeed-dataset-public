# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst)!=1:
        return max(lst[0], max_recursive(lst[1:]))
    else:
        return lst[0]
    

print(max_recursive([2, 8, 6]))


def sum_lists_recursive(lst1, lst2):
    if len(lst1)!=0 and len(lst2)!=0:
        return lst1[0]+ lst2[0]+ sum_lists_recursive(lst1[1:], lst2[1:])
    else:
        return 0

print(sum_lists_recursive([2, 3], [5, 6]))


def funky(n):
    if n==1 or n==0:
        return 1
    elif n%2==0:
        return 2*funky(n//2)
    else:
        return 1+ 2*funky(n+1)

print(funky(10))