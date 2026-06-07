# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    if n <= 0:
        return
    for start in range(n, 0, -1):
        print(" ".join(str(i) for i in range(start, 0, -1)))

def merge_dicts(d1,d2):
    result = d1.copy()
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result

