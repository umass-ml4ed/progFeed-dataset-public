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
    max_recursive (lst)
