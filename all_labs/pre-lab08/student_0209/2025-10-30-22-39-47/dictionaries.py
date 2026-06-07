# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    if not frequency:
        return None
    most_frequent = max(frequency, key=frequency.__getitem__)
    return most_frequent

print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
# 2

print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
# 'apple'

print(most_frequent_element([1, 2, 3, 4]))
# 1, 2, 3, or 4 (any valid answer)

print(most_frequent_element([]))
# None

def greet_user(user_info):
    name = user_info.get("name", "Guest")
    age = user_info.get("age", "unknown age")
    city = user_info.get("city", "unknown city")
    print(f"Hello, {name}! You are {age} years old and live in {city}.")
