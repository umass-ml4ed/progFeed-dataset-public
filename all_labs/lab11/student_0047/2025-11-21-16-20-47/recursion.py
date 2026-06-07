# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst)==1:
        return lst[0]
    elif lst==[]: 
        return 0
    else:
        max=max_recursive(lst[1:])
        if max<=lst[0]:
            max=lst[0]
        return max

def sum_lists_recursive(lst1,lst2):
    if lst1==[]:
        return 0
    else:
        s=sum_lists_recursive(lst1[1:],lst2[1:])
        s+=lst1[0]
        s+=lst2[0]
        return s

def funky(n):
    if n==1 or n==0:
        return 1
    elif n%2==0:
        f=2*funky(n//2)
        return f
    else:
        f=1+2*funky(n+1)
        return f
        

