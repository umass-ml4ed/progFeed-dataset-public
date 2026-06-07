# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(lst):
    newlst = []
    for i in lst:
        if i > 0:
            newlst.append(i)
    return newlst

#print(filter_positive([1, -3, 5, 0, -2, 7]))
#print(filter_positive([-5, -1, -10]))
#print(filter_positive([10, 20, -30, 40]))