# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    for x in range(n,0,-1):
        lst=[]
        while x>=1:
            lst.append(str(x))
            x-=1
        print(" ".join(lst))

def merge_dicts(d1,d2):
    d=d1.copy()
    for k,v in d2.items():
        if k in d:
            d[k]+=v
        else:
            d[k]=v
    return d
