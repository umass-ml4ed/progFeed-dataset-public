#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def pyramid(n):
    pyramid = ''
    for i in range (n,0,-1):
        for j in range(i,0,-1):
            pyramid += f'{j} '
        pyramid += '\n'
    return pyramid

def merge_dicts(d1,d2):
    merged = d1.copy()
    for i in d2:
        if i in d1:
            merged[i] += d2[i]
        else:
            merged.update({i: d2[i]})
    return merged      