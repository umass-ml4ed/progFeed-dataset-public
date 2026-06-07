# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    patt=''
    for i in range(n,0,-1):
        num=''
        for j in range(i,0,-1):
            num=num+' '+str(j)
        patt=patt+(num+'\n')
    return patt


def merge_dicts(d1,d2):
    new_d={}
    for key in d1:
        if key in d2:
            n=d1[key]+d2[key]
            new_d[key]=n
        else:
            new_d[key]=d1[key]
    for key_2 in d2:
        if key_2 not in d1:
            new_d[key_2]=d2[key_2]
    return new_d

print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))

    