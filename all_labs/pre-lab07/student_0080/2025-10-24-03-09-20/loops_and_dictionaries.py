# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    result = ""
    for i in range(n, 0, -1):
        # Create numbers from current i down to 1
        line = []
        for j in range(i, 0, -1):
            line.append(str(j))
        result += " ".join(line) + "\n"
    return result

def merge_dicts(d1, d2):
    result = d1.copy()  # Start with a copy of d1
    
    for key, value in d2.items():
        if key in result:
            result[key] += value  # Sum if key exists in both
        else:
            result[key] = value   # Add new key-value pair
    
    return result

print("Testing pyramid function:")
print(pyramid(4))
print(pyramid(5))

print("\nTesting merge_dicts function:")
print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dicts({'x': 10}, {'y': 20}))
print(merge_dicts({}, {'a': 5}))
print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))