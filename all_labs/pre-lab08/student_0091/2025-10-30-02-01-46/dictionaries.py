def most_frequent_element(lst):
    if not lst:  
        return None

    counts = {}

    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    max_count = 0
    most_frequent = None
    for key in counts:
        if counts[key] > max_count:
            max_count = counts[key]
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

