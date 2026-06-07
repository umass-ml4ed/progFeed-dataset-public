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
    lst1.remove (l1)
    lst2.remove (l2)
    return l1 + l2 + sum_lists_recursive (lst1, lst2)
print (sum_lists_recursive([1, 2, 3], [4, 5, 6]))
print (sum_lists_recursive([],[])     )