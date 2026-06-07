# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def filter_positive(int_list):
    positive_list = []
    for i in int_list:
        if i > 0:
            positive_list.append(i)
    return positive_list


print(filter_positive([1, -3, 5, 0, -2, 7]))

