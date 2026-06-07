# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


def pyramid(n):
    lines=''
    for a in range(n,0,-1):
        line=''
        for b in range(a,0,-1):
            line+=str(b)
            line+=' '
        lines+=line[:-1] +'\n'
    return lines

def merge_dicts(d1,d2):
    new_dict={}
    for key in d1:
        if key in d2:
            new_dict[key]=d1[key]+d2[key]
        else:
            new_dict[key]=d1[key]
    for key in d2:
        if key in d1:
            new_dict[key]=d1[key]+d2[key]
        else:
            new_dict[key]=d2[key]
    return new_dict

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dicts({'x': 10}, {'y': 20}))
print(merge_dicts({}, {'a': 5}))
print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))

