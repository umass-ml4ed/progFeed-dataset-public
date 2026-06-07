# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    for i in range(n, 0, -1):
        print(' '.join(str(j) for j in range(i, 0, -1)))

def merge_dicts(d1, d2):
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged
