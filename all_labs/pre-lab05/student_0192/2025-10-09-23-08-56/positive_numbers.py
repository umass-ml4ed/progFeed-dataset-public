def filter_positive(x):
    lst = []
    for i in x:
        if i>0:
            lst.append(int(i))
    return lst


print(filter_positive([1, -3, 5, 0, -2, 7]))
# [1, 5, 7]

print(filter_positive([-5, -1, -10]))
# []

print(filter_positive([10, 20, -30, 40]))


