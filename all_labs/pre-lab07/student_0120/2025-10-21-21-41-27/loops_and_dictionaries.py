# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED

def pyramid(n):
    for i in range(n, 0, -1):
        line = ' '.join(str(j) for j in range(i, 0, -1))
        print(line)

print(pyramid(4))
print(pyramid(5))

def merge_dicts(d1, d2):
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] += value  
        else:
            result[key] = value 
    return result
    
print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
# {'a': 1, 'b': 5, 'c': 4}

print(merge_dicts({'x': 10}, {'y': 20}))
# {'x': 10, 'y': 20}

print(merge_dicts({}, {'a': 5}))
# {'a': 5}

print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))
# {'a': 1, 'b': 7, 'c': 3, 'd': 10}

