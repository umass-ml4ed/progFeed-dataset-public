# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def max_recursive(lst):
    if len(lst)==1:
        return lst[0]
    if len(lst)==0:
        return
    s=max_recursive(lst[1:])
    if lst[0]>s:
        return lst[0]
    else:
        return s
print(max_recursive([3, 10, 2, 8, 6]))

def sum_lists_recursive(lst1, lst2):
    if len(lst1)==0 and len(lst2)==0:
        return 0
    if len(lst1)==1 and len(lst2)==1:
        return lst1[0]+lst2[0]
    x=sum_lists_recursive(lst1[1:], lst2[1:])
    return lst1[0]+lst2[0]+x
print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))

def funky(n):
    if n==0 or n==1:
        return 1
    if n%2==0:
        return 2*funky(n//2)
    else:
        return 1+2*funky(n+1)
print(funky(-51))