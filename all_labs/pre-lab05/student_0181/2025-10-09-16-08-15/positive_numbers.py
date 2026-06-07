# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(a : list):
    lst = []
    for i in a :
        if i > 0:
            lst.append(i)
    return lst
print(filter_positive([1, -3, 5, 0, -2, 7]))




