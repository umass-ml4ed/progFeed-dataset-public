# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    while n>0:
        h=n
        while h>0:
            print(f"{h} ", end = '')
            h-=1
        print()
        n-=1

def merge_dicts(d1,d2):
    newdict = d1.copy()
    for i,j in d2.items():
        if i in newdict:
            newdict[i] += j
        else:
            newdict[i] = j
    return newdict

