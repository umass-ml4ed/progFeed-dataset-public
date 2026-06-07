def filter_positive(L):
    positive = []
    for num in L:
        if num > 0:
            positive.append(num)
    return positive
print(filter_positive([1, -3, 5, 0, -2, 7]))
print(filter_positive([-5, -1, -10]))
print(filter_positive([10, 20, -30, 40]))