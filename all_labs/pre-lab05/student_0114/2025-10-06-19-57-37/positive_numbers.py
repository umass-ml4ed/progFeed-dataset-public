# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(lst):
    pos_lst = []
    for x in lst:
        if x > 0:
            pos_lst.append(x)
    return pos_lst

print(filter_positive([1, -3, 5, 0, -2, 7]))
# [1, 5, 7]

print(filter_positive([-5, -1, -10]))
# []

print(filter_positive([10, 20, -30, 40]))
# [10, 20, 40]
