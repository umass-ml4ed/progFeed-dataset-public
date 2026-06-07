# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst)<2:
        return len(lst)
    z=2
    for i in range(2, len(lst)):
        diff1=lst[i-1]-lst[i-2]
        diff2=lst[i]-lst[i-1]
        if diff1*diff2<0:
            z+=1
        else:
            break
    return z

def zigzag_lengths_from_all_starts(lst):
    if len(lst)==2:
        return []
    if len(lst)==1:
        return [1]
    z=[]
    for i in range(len(lst)):
        if i==len(lst)-1:
            z.append(1)
        else:
            x=2
            for j in range(i+2, len(lst)):
                diff1=lst[j-1]-lst[j-2]
                diff2=lst[j]-lst[j-1]
                if diff1*diff2<0:
                    x+=1
                elif lst[1]-lst[0]==0:
                    x-=1
                else:
                    break
            z.append(x)
    return z

