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
sum = 0
def sum_lists_recursive (lst1, lst2):
    global sum
    sum += lst1[0]
    sum += lst2[0]
    lst1.remove (lst1[0])
    lst2.remove (lst2[0])
    if len (lst1) and len (lst2) == 0:
        return sum
    else:
        return sum_lists_recursive
print (sum_lists_recursive([1, 2, 3], [4, 5, 6]))