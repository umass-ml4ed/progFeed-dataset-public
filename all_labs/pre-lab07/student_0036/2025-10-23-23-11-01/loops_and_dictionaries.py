# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    pyramid=""
    for i in reversed(range(n)):
        for j in reversed(range(1,i+2)):
            pyramid+=str(j)
            if j!=1:
                pyramid+=" "
        pyramid+="\n"
    return pyramid


def merge_dicts(d1:dict,d2:dict):
    merged={}
    for key in set(d1.keys()).union(d2.keys()):
        if key in d1 and key in d2:
            merged[key]=(d1[key]+d2[key])
        elif key in d1:
            merged[key]=d1[key]
        else:
            merged[key]=d2[key]
    return merged

#print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
# {'a': 1, 'b': 5, 'c': 4}

#print(merge_dicts({'x': 10}, {'y': 20}))
# {'x': 10, 'y': 20}

#print(merge_dicts({}, {'a': 5}))
# {'a': 5}

#print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))
# {'a': 1, 'b': 7, 'c': 3, 'd': 10}
