# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def  pyramid(n):
    result=""
    for i in range(n,0,-1):
        l=""
        for j in range(i,0,-1):
            l+=str(j)
            if j!=1:
                l+=""
        result+=l
        if i!=1:
            result+="\n"
    return result

print(pyramid(4))
print(pyramid(5))

def merge_dicts(d1,d2):
    result={}
    for i in d1:
        result[i]=d1[i]
    for j in d2:
        if j in result:
            result[j]+=d2[j]
        else:
            result[j]=d2[j]
    return result

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dicts({'x': 10}, {'y': 20}))
print(merge_dicts({}, {'a': 5}))
print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))