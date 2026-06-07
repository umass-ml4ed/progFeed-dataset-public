# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    for i in range(n,0,-1):
        for l in range(i,0,-1):
            print(f" {l} ",end="")
        print()

def merge_dicts(d1,d2):
    d1.update(d2)
    return d1

pyramid(5)
print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))
