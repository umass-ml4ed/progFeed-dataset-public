# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    for i in range(n, 0, -1):
        line = ''
        for j in range(i, 0, -1):
            line += str(j) + ' '
        print(line.strip())

def merge_dicts(d1, d2):
    result = d1.copy()
    for key in d2:
        if key in result:
            result[key] += d2[key]
        else:
            result[key] = d2[key]
    return result


# pyramid(4)
# print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))