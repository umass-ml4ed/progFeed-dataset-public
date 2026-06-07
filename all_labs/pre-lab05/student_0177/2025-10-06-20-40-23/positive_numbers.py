# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def filter_positive(a:list) :
    pos_list=[]
    for num in a :
        if num>0:
            pos_list.append(num)
    return pos_list

print(filter_positive([1, -3, 5, 0, -2, 7]))
# [1, 5, 7]

print(filter_positive([-5, -1, -10]))
# []

print(filter_positive([10, 20, -30, 40]))
# [10, 20, 40]
