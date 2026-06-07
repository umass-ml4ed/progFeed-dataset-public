# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    full_lst=[]
    for x in range(n,0,-1):
        lst=[]
        while x>=1:
            lst.append(str(x))
            x-=1
        numbers=" ".join(lst)
        full_lst.append(numbers)
    return "\n".join(full_lst)

def merge_dicts(d1,d2):
    d=d1.copy()
    for k,v in d2.items():
        if k in d:
            d[k]+=v
        else:
            d[k]=v
    return d
