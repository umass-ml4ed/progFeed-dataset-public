# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(elements):
    the_dict = {item: elements.count(item) for item in elements}
    max_value = 0
    max_key = None
    for key in the_dict:
        try:
            if the_dict[key] > max_value:
                max_value = the_dict[key]
                max_key = key
        except UnboundLocalError:
            max_key
    return max_key

print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
# 2

print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
# 'apple'

print(most_frequent_element([1, 2, 3, 4]))
# 1, 2, 3, or 4 (any valid answer)

print(most_frequent_element([]))
# None
