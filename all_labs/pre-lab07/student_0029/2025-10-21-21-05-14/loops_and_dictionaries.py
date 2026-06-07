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
    return result.strip()

print(pyramid(4))

def merge_dicts(d1,d2):
    merged = {}
    for key in d1:
        if key in d2:
            merged[key] = d1[key] + d2[key]
        else:
            merged[key] = d1[key]
    for key in d2:
        if key not in d1:
            merged[key] = d2[key]
    return merged