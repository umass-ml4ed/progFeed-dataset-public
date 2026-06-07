# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    for i in range(n,0,-1):
            line = ' '.join(str(j) for j in range(i, 0, -1))
            print(line)

print(pyramid(5))

def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged