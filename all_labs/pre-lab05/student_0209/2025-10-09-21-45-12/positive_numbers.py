# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def filter_positive(int):
    int_list = []
    for i in int:
        if i >= 0:
            int_list.append(i)
    return int_list


print(filter_positive([1, -3, 5, 0, -2, 7]))

