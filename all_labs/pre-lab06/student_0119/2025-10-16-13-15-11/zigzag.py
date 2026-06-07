# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# def is_zigzag(lst):
#     if len(lst)<3:
#         return True
#     i=1
#     for i in range(1, len(lst) - 1):
#         if not ((lst[i]>lst[i+1] and lst[i]>lst[i-1]) or (lst[i]<lst[i+1] and lst[i]<lst[i-1])):
#             return False
#     return True

def longest_zigzag_from_start(lst):
    if len(lst)<2:
        return len(lst)
    x=0
    length=1
    for i in range(1,len(lst)):
        diff=lst[i]-lst[i-1]
        if diff==0:
            break
        if diff>0:
            y=1
        else:
            y=-1
        if x==0 or y!=x:
            length+=1
            x=y
        else:
            break
    return length

def zigzag_lengths_from_all_starts(lst):
    if len(lst)==0:
        return []
    if len(lst)==1:
        return[1]
    result=[]
    for start in range(len(lst)):
        x=0  
        length = 1
        for i in range(start+1,len(lst)):
            diff=lst[i]-lst[i-1]
            if diff==0:
                break
            if diff>0:
                y=1
            else:
                y=-1
            if x==0 or y!=x:
                length+=1
                x=y
            else:
                break
        result.append(length)
    return result

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))