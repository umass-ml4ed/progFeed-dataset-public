# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    result = ""
    for i in range(n, 0, -1):
        line = ""
        for j in range(i, 0, -1):
            line += str(j) + " "
        result += line.strip() + "\n"
    return result

def merge_dicts(d1, d2):
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

# -----------------------
# Test the functions
# -----------------------
print(pyramid(4))
print(pyramid(5))

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dicts({'x': 10}, {'y': 20}))
print(merge_dicts({}, {'a': 5}))
print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))