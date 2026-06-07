# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    lines = []
    for i in range(n, 0, -1):
        line = ' '.join(str(x) for x in range(i, 0, -1))
        lines.append(line)
    return '\n'.join(lines)
print(pyramid(4))
print(pyramid(5))

def merge_dicts(d1, d2):
    new = d1.copy()
    for key, value in d2.items():
        if key in new:
            new[key] += value
        else: 
            new[key] = value
    return new
print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dicts({'x': 10}, {'y': 20}))
print(merge_dicts({}, {'a': 5}))
print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))

