# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst : list) -> bool:
    count = 0
    if len(lst) < 3:
        return True
    for i in range(1,len(lst)-1):
        if (lst[i] > lst[i+1] and lst[i] > lst[i-1]) or (lst[i] < lst[i+1] and lst[i] < lst[i-1]):
            count = count + 1
    if count == len(lst)-2:
        return True
    else:
        return False
    

    

