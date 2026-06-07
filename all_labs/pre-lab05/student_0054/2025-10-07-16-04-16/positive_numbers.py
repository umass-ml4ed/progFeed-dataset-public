# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def filter_positive(list):
    positive_number_list = []
    for i in list:
        if i > 0:
            positive_number_list.append(i)
    return positive_number_list

print(filter_positive([1, -3, 5, 0, -2, 7])) # [1, 5, 7]
print(filter_positive([-5, -1, -10])) # []
print(filter_positive([10, 20, -30, 40])) # [10, 20, 40]