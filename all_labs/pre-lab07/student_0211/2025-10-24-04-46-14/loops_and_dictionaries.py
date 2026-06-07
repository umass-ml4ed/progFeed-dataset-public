# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    result = ""
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            result += str(j) 
            if j != 1:
                result += " "
        result += "\n"
    return result  

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


print(pyramid(4))
print(pyramid(5))
print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
