# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(lst):
    positivenums=[]
    for num in lst:
        if num>0:
            positivenums.append(num)
    return positivenums

print(filter_positive([1, -3, 5, 0, -2, 7]))
print(filter_positive([-5, -1, -10]))
print(filter_positive([10, 20, -30, 40]))
