# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(lis):
    new_lis = []
    for i in lis:
        if lis[i] > 0:
            new_lis.append(lis[i])
    
    return new_lis

print(filter_positive([1, -3, 5, 0, -2, 7]))