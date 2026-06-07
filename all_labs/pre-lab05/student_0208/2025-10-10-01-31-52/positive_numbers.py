# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def filter_positive(numbers):
    positive_list=[]
    for n in numbers:
        if n>0:
            positive_list.append(n)
    return positive_list

print(filter_positive([1,-3,5,0,-2,7]))