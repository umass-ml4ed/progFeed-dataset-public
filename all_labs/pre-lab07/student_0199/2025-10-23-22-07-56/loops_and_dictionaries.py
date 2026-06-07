# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    structure = ""
    for line in range(n, 0, -1):
        for number in range(line, 0, -1):
            structure += str(number) + " "
        structure += "\n"
    return structure

def merge_dicts(d1, d2):
    d3 = d1.copy()
    for k in d1:
        if k in d2:
            d3[k] = d1[k] + d2[k]
    for k in d2: 
        if k not in d1:
            d3[k] = d2[k]
    return d3

#print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
# {'a': 1, 'b': 5, 'c': 4}

#print(merge_dicts({'x': 10}, {'y': 20}))
# {'x': 10, 'y': 20}

#print(merge_dicts({}, {'a': 5}))
# {'a': 5}

#print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))
# {'a': 1, 'b': 7, 'c': 3, 'd': 10}

