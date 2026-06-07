# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(l):
    nl = []
    for num in l:
        if num > 0:
            nl.append(num)
    return nl

print(filter_positive([1, -3, 5, 0, -2, 7]))
print(filter_positive([-5, -1, -10]))