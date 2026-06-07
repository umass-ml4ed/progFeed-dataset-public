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
    z=[]
    if len(lst)<2:
        return [len(lst)]
    for i in range(2, len(lst)+1):
        x=2
        for j in range(i, len(lst)):
            diff1=lst[j-1]-lst[j-2]
            diff2=lst[j]-lst[j-1]
            if diff1*diff2<0:
                x+=1
            elif i==len(lst):
                x-=1
            else:
                break
        z.append(x)
    z.append(1)
    return z

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]

print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]

print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]

print(zigzag_lengths_from_all_starts([10]))  # [1]
