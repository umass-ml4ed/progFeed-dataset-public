# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    while n >= 1:
        it = 0
        while n - it >= 1:
            if n - it == 1:
                print(str(n-it))
                it += 1
            else:
                print(str(n-it),end=' ')
                it += 1
        n -= 1
    return

def merge_dicts(d1, d2):
    n1 = {}
    for key in d1:
        if key in d2:
            n1[key] = (d1[key]+d2[key])
        else:
            n1[key] = (d1[key])
    for key in d2:
        if key not in d1:
            n1[key] = (d2[key])
    return n1



print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))