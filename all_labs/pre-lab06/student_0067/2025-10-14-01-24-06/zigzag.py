# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    if lst[0]>lst[1]:
        current = "down"
    else:
         current = "up"
    count = 1
    
    for i in range(1,len(lst)):
        if current=="up" and lst[i-1]<lst[i]:
            count +=1
            current = "down"
        elif current == "down" and lst[i-1]>lst[i]:
            count +=1
            current = "up"
        else: 
            break
    return count


def zigzag_lengths_from_all_starts(lst: list) -> list:
    if len(lst) == 0:
        return []
    
    z_lengths = []
    for i in range(len(lst)):
       
        sub = lst[i:]
        if len(sub) < 2:
            z_lengths.append(len(sub))
        else:
            z_lengths.append(longest_zigzag_from_start(sub))
    return z_lengths
        