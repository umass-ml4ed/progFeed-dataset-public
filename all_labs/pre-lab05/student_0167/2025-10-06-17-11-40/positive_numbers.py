# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(integers_list):
    new_list = []
    for i in range(0,len(integers_list)):
        if integers_list[i] > 0:
            new_list.append(integers_list[i])
    return new_list

print(filter_positive([1, -3, 5, 0, -2, 7]))
# [1, 5, 7]

print(filter_positive([-5, -1, -10]))
# []

print(filter_positive([10, 20, -30, 40]))
# [10, 20, 40]
