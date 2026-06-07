# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n): 
    result = ""
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            result += str(j) + ' '
        result += '\n'
    return result

print(pyramid(4))

def merge_dicts(d1, d2):
    merged = d1.copy()
    for key in d2:
        if key in merged:
            merged[key] += d2[key]
        else:
            merged[key] = d2[key]
        
    return merged

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
# {'a': 1, 'b': 5, 'c': 4}

print(merge_dicts({'x': 10}, {'y': 20}))
# {'x': 10, 'y': 20}

print(merge_dicts({}, {'a': 5}))
# {'a': 5}

print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))
# {'a': 1, 'b': 7, 'c': 3, 'd': 10}
