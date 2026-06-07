# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def pyramid(n):
    for i in range (n, 0, -1):
        line = ' '.join(str(num) for num in range (i, 0, -1))
        print (line)
    print()
pyramid(5)

def merge_dicts(d1, d2):
    merged = {}
    for key in d1:
        merged[key] = d1[key]
    for key in d2:
        if key in merged:
            merged [key] += d2[key]
        else:
            merged[key] = d2[key]
    return merged
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'b':3, 'c':4, 'd':5}
result = merge_dicts(dict1, dict2)
print (result)