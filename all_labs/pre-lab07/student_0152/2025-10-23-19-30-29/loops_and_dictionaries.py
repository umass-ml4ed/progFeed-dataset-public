# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    for i in range(n, 0, -1):
        line = ' '.join(str(j) for j in range(i, 0, -1))
        print(line)

pyramid(4)
pyramid(5)

def merge_dicts(d1, d2):
    result = d1.copy()
    for key in d2:
        if key in result:
            result[key] += d2[key]
        else:
            result[key] = d2[key]
    return result

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dicts({'x': 10}, {'y': 20}))
print(merge_dicts({}, {'a': 5}))
print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))
