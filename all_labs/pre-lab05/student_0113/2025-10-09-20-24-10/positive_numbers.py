#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def filter_positive(lst):
    new_lst = []
    for i in range(len(lst)):
        if lst[i] > 0: 
            new_lst.append(lst[i])
    return new_lst


print(filter_positive([1, -3, 5, 0, -2, 7]))
# [1, 5, 7]

print(filter_positive([-5, -1, -10]))
# []

print(filter_positive([10, 20, -30, 40]))
# [10, 20, 40]
