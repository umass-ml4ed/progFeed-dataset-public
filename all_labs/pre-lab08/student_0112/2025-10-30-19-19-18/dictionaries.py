# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def most_frequent_element(lst):
    dct = {}
    if (len(lst) == 0):
        return  None
    else:
        for i in range (len(lst)):
            if lst[i] not in dct:
                dct[lst[i]] = 1
            else:
                dct[lst[i]] += 1
        max = 0
        for key, count in dct.items():
            if count > max:
                max = count
                max_value_item = key
        return max_value_item

        
print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
# 2

print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
# 'apple'

print(most_frequent_element([1, 2, 3, 4]))
# 1, 2, 3, or 4 (any valid answer)

print(most_frequent_element([]))
# None
