# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):

    if len(lst)<=1:
        return len(lst)
    length=1
    next=None

    for i in range(1, len(lst)):
        if lst[i]==lst[i-1]:
            break
        if next is None:
            next=lst[i]>lst[i-1]
            length+=1
        elif (next and lst[i]<lst[i-1]) or (not next and lst[i]>lst[i-1]):
            next=not next
            length+=1
        else:
            break
    return length


def zigzag_lengths_from_all_starts(lst):
    new_list=[]

    for first in range(len(lst)):
        length=1
        direction=None

        for i in range(first+1, len(lst)):
            if lst[i]==lst[i-1]:
                break
                
            if direction is None:
                direction =lst[i]>lst[i-1]
                length+=1
            elif (direction and lst[i]<lst[i-1]) or (not direction and lst[i]>lst[i-1]):
                direction =not direction
                length+=1
            else:
                break
        new_list.append(length)
    return new_list

print(zigzag_lengths_from_all_starts([1,2,3,4,5]))