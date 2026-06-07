# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def longest_zigzag_from_start(lst):
    if len(lst)<2:
        return len(lst)
    else:
        z=[]
        for i in range(1,len(lst)+1):
            z=lst[:i]
            for n in range(1,len(z)-1):
                if z[n]>z[n+1] and z[n]>z[n-1] or z[n]<z[n+1] and z[n]<z[n-1]:
                    continue
                else:
                    return len(z)-1
        return len(z)

def zigzag_lengths_from_all_starts(lst):
    lst1=[]
    for i in range(len(lst)):
        z=lst[i:]
        lst1.append(longest_zigzag_from_start(z))
    return lst1


