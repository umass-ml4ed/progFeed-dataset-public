# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
integers=[]
def filter_positive(integers):
    positive=[]
    for integer in integers:
        if integer>0:
            positive.append(integer)
    return positive


print(filter_positive([1, -3, 5, 0, -2, 7]))
# [1, 5, 7]

print(filter_positive([-5, -1, -10]))
# []

print(filter_positive([10, 20, -30, 40]))
# [10, 20, 40]
