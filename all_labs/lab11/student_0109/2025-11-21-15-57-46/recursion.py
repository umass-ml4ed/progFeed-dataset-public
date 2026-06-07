#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def max_recursive(lst):
    if not lst:
        return 0
    elif len(lst)==1:
        return lst[0]
    else:
        if lst[0] > lst[1]:
            lst.remove(lst[1])
        else:
            lst.remove(lst[0])
        return max_recursive(lst)

def sum_lists_recursive(lst1,lst2):
    if len(lst1) == 0:
        return 0
    else:
        sm = lst1[0] + lst2[0]
        # lst1.remove(lst1[0])
        # lst2.remove(lst2[0])
        return sm + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if (not n) or (n==1):
        return 1
    if not n%2:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n+1)