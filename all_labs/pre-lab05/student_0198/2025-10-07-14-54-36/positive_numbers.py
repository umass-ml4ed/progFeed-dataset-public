# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def filter_positive(lst:list):
    lst2 = []
    for ch in lst:
        if ch >0:
            lst2.append(ch)
    return lst2
print(filter_positive([1, -3, 5, 0, -2, 7]))
