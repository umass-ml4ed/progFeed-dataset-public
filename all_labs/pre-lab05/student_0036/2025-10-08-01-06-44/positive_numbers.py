# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(a: list):
    lst=[]
    for i in a:
        if i>0:
            lst.append(i)
    return lst

print(filter_positive([1, -3, 5, 0, -2, 7]))
# [1, 5, 7]

print(filter_positive([-5, -1, -10]))
# []

print(filter_positive([10, 20, -30, 40]))
# [10, 20, 40]
