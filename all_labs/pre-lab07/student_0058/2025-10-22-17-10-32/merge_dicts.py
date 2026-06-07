# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def merge_dicts(d1, d2):
    new_dict = d1.copy() 
    for key, value in d2.items():   
        if key in new_dict:
            new_dict[key] += value 
        else:
            new_dict[key] = value   
    
    return new_dict
    
print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dicts({'x': 10}, {'y': 20}))
print(merge_dicts({}, {'a': 5}))
print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))