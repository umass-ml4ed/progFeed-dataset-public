# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j, end=' ')
        print()   

def merge_dicts(d1,d2):
    merged = {}
    for key in d1:
       merged[key] = d1[key]
    for key in d2:
        if key in merged:
            merged[key] += d2[key]
        else:
            merged[key] = d2[key]
    return merged


pyramid(4)
pyramid(5)
print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
