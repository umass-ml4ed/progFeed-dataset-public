# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

#pyramid

def pyramid(n):
    result = []
    for i in range(n, 0, -1):
        line = ' '.join(str(x) for x in range(i, 0, -1))
        result.append(line)
    return '\n'.join(result)

print(pyramid(4))
print()
print(pyramid(5))

#merge_dicts

def merge_dicts(d1, d2):
    merged = d1.copy()  
    for key, value in d2.items():
        if key in merged:
            merged[key] += value 
        else:
            merged[key] = value 
    return merged

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})) 
print(merge_dicts({'x': 10}, {'y': 20}))               
print(merge_dicts({}, {'a': 5}))                        
print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10})) 

