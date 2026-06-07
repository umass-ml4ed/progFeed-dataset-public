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
#max_recursive([8, 6])           # returns 8
#ax_recursive([6])  
