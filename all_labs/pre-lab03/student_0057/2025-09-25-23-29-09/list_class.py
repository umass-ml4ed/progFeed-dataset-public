# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

#1. combine lists

def combine_lists(a, b):
    a.insert(0, b[0])
    a.append(b[-1])
    mid = len(a) // 2
    del a[mid]
    return a
print(combine_lists([1, 2, 3],[4, 5, 6, 7]))
print(combine_lists([1, 2, 3, 4, 5],[4, 5, 6, 7]))

#2. classify by length

def classify_by_length(a):
    if len(a) == 0:
        return "empty"
    elif len(a) % 2 == 0:
        return "even_length"
    else:
        return "odd_length"
print(classify_by_length([1, 2, 3]))
print(classify_by_length([1, 2, 2, 3]))
print(classify_by_length([]))