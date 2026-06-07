# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    final = []
    while n > 0:
        lst = []
        for i in range(1, n+1):
            lst.append(str(i))
        lst.reverse()
        result = " ".join(lst)
        #print(result) # debug: prints each result
        final.append(result)
        n += -1
    #print(final) # debug: prints list containing all results
    return "\n".join(final)

#print(pyramid(4))
#print(pyramid(5))
#print(pyramid(3))

def merge_dicts(d1, d2):
    new_dict = {}
    for key in d1:
        if key in d2:
            new_dict[key] = d1[key] + d2[key]
        else:
            new_dict[key] = d1[key]
    for key in d2:
        if key not in d1:
            new_dict[key] = d2[key]
    return new_dict

#print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
#print(merge_dicts({'x': 10}, {'y': 20}))
#print(merge_dicts({}, {'a': 5}))
#print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))