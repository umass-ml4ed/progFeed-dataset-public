# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(a):
    lst = []
    for i in a:
        if i > 0:
            lst.append(i)
    return lst

print(filter_positive([-3, -2]))
