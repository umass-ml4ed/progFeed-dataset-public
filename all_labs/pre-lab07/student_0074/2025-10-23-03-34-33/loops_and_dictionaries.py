# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(num):
    for i in range(num, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')  
        print()  

#pyramid(5)
#pyramid(15)
#pyramid(21)

def merge_dicts(d1, d2):
    carboncopy = d1.copy()  

    for i in d2:
        if (i in carboncopy):
            carboncopy[i] += d2[i]
        else:
            carboncopy[i] = d2[i]
    return carboncopy

#print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
#print(merge_dicts({'x': 10}, {'y': 20}))
#print(merge_dicts({}, {'a': 5}))
#print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))

