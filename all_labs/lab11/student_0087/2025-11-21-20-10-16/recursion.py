# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive (lst):
    if len (lst) == 1:
        return lst[0]
    if len (lst) == 0:
        return 0
    if lst[0] > lst[1]:
        lst.remove (lst[1])
    else:
        lst.remove (lst[0])
    return max_recursive (lst)
#print (max_recursive([3, 10, 2, 8, 6])) # returns 10
#print (max_recursive([10, 2, 8, 6]))    # returns 10
#print (max_recursive([2, 8, 6]))        # returns 8

def sum_lists_recursive (lst1, lst2):
    if len (lst1) == 0 and len (lst2) == 0:
        return 0
    l1 = lst1[0]
    l2 = lst2[0]
    return l1 + l2 + sum_lists_recursive (lst1[1:], lst2[1:])
#print (sum_lists_recursive([1, 2, 3], [4, 5, 6]))
#print (sum_lists_recursive([],[]))

def funky (n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * funky (n//2)
    else:
        return 1 + 2 * funky (n+1)
print (funky(2))