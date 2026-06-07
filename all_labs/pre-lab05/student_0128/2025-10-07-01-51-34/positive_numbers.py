# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def filter_positive(int_list):
    positive_list = []
    for num in int_list:
        if num > 0:
            positive_list.append(num)
    return positive_list
print(filter_positive([10, 20, -30, 40]))