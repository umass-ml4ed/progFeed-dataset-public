# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    str = ""
    while n>0:
        h=n
        while h>0:
            str += f"{h} "
            h-=1
        if n>1: 
            str += "\n"
        n-=1
    return str

def merge_dicts(d1,d2):
    newdict = d1.copy()
    for i,j in d2.items():
        if i in newdict:
            newdict[i] += j
        else:
            newdict[i] = j
    return newdict

print(pyramid(4))