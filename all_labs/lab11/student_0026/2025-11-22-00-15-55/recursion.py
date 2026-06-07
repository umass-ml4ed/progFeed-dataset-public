# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if len(lst)==0:
        return 0
    if len(lst)==1:
        return lst[0]
    prev= max_recursive(lst[1:])
    if lst[0] > prev:
        return lst[0]
    else:
        return prev

print(max_recursive([3]))

def sum_lists_recursive(lst1, lst2):
    if len(lst1) ==0  and len(lst2)==0:
        return 0
    sum = lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])
    return sum

print(sum_lists_recursive([1], [4]))

def funky(n):
    if n == 0 or n==1:
        return 1
    if n%2==0:
        