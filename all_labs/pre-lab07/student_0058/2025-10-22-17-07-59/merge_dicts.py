# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def merge_dicts (d1, d2):
    new_dict = {}
    
    for key1 in d1 :
            if key1 in d2:
                new_dict[key1] = d1[key1] + d2[key1]
            else: 
                new_dict[key1] = d1[key1]
    for key2 in d2:
         if key2 not in new_dict:
              new_dict[key2] = d2[key2]
    return new_dict

    
print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dicts({'x': 10}, {'y': 20}))
print(merge_dicts({}, {'a': 5}))
print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))