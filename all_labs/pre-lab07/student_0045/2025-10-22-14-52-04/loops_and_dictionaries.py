# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    result = ""
    for i in range(n):
        line1 = [str(x) for x in range(n-i, 0, -1)]
        result+=' '.join(line1) + "\n"
    return result

print(pyramid(4))

def merge_dicts(d1: dict, d2: dict):
    result = d1.copy()
    for item in d2:
        if item in result:
            result[item]+=d2[item]
        else:
            result[item] = d2[item]
    return result

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
