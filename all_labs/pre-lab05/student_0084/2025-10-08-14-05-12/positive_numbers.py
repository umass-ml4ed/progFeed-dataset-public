# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

#3 Implement filter_positive
def filter_positive(l):
    positive_list = []
    for item in l:
        if item > 0:
            positive_list.append(item)
    return positive_list

print(filter_positive([1, -3, 5, 0, -2, 7]))
# [1, 5, 7]

print(filter_positive([-5, -1, -10]))
# []

print(filter_positive([10, 20, -30, 40]))
# [10, 20, 40]