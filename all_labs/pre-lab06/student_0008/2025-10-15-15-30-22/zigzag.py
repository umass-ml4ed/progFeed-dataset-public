# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    x = lst[1] - lst[0]
    if x == 0:
        count = 1
    else:
        count = 2
    for i in range(2, len(lst)):
        y = lst[i] - lst[i-1]
        if y == 0:
            continue
        if x == 0 or x * y < 0:
            count +=1
        x = y
    return count

def zigzag_lengths_from_all_starts(lst):
    newLst = []
    for i in range(len(lst)):
        count = 0
        if i == len(lst) - 1:
            newLst.append(1)
            continue
        x = lst[i+1] - lst[i]
        if x == 0:
            newLst.append(1)
            continue
        count += 1
        for j in range(i+1, len(lst)-1):
            y = lst[j+1] - lst[j]
            if y == 0 or x * y > 0:
                break
            count += 1
            x = y
        newLst.append(count+1)
    return newLst
