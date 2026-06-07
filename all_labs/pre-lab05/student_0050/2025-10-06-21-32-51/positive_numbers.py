# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(lis)->[]:
    pos = []
    for i in range(0,len(lis)):
        if(lis[i]>0):
            pos.append(lis[i])
        i=+1
    return pos




print(filter_positive([1, -3, 5, 0, -2, 7]))
# [1, 5, 7]

print(filter_positive([-5, -1, -10]))
# []

print(filter_positive([10, 20, -30, 40]))
# [10, 20, 40]
