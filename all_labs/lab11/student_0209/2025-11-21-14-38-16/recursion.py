# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if not lst:
        return 0
    if len(lst) ==1:
        return lst[0]
    else:
        max= max_recursive(lst[1:])
        return lst[0] if lst[0]>max else max

def sum_lists_recursive(lst1, lst2):
    if not lst1 and not lst2:
        return 0
    else:
        return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])
    
def funky(n):
    if n==1 or n==0:
        return 1
    if n%2==0:
        return funky(n//2)*2
    else:
        return 1 + 2*funky(n+1)
    

