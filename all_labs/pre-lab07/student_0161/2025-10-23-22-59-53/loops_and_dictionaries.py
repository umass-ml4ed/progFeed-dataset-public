# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    lst=[]
    for i in range(n,0,-1):
        lst.append("\n")
        for l in range(i,0,-1):
            lst.append(f"{l} ")
    return "".join(lst)

def merge_dicts(d1,d2):
    d1_copy = d1 | d2
    return d1_copy

print(pyramid(4))
print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))
