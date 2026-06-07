# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
import math
import random
def max_recursive(lst):
    if len(lst)==1:
        return lst[0]
    max=max_recursive(lst[1:])
    if lst[0]>max:
        return lst[0]
    else:
        return max
def sum_lists_recursive(lst1, lst2):
    if len(lst1)==0:
        return 0
    else:
        return lst1[0]+lst2[0]+sum_lists_recursive(lst1[1:],lst2[1:])
def funky(n):
    if n==0 or n==1:
        return 1
    elif n%2==0:
        return 2*funky(n // 2)
    else:
        return 1+2*funky(n+1)