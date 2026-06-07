def filter_positive(n):
    positives = []
    for i in n:
        if (i > 0):
            positives.append(i)
    return positives

#print(filter_positive([1, -3, 5, 0, -2, 7]))
#print(filter_positive([-5, -1, -10]))
#print(filter_positive([10, 20, -30, 40]))

