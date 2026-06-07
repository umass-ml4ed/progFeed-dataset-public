# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    result = ""
    for i in range(n, 0, -1):
        line = " ".join(str(j) for j in range(i, 0, -1))
        result += line + "\n"
    return result
def merge_dicts(d1,d2):
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))







