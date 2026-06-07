# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

def most_frequent_element(lst):
    count = {}
    for i in lst:
        if i in count:
            count[i] += 1
        else: 
            count[i] = 1
    counts = 0
    most_frequent = None
    for key in count:
        if count[key] > counts:
            counts = count[key]
            most_frequent = key

    return most_frequent

print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
# 2

print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
# 'apple'

print(most_frequent_element([1, 2, 3, 4]))
# 1, 2, 3, or 4 (any valid answer)

print(most_frequent_element([]))
# None
