# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag (lst): 
    b = len(lst) -2
    zig = True
    for i in range(1, b): 
        if lst[i]>lst[i+1] and lst[i]>lst[i-1]: 
            continue
        elif lst[i]<lst[i+1] and lst[i]<lst[i-1]:
            continue
        else: 
            zig = False
            break
    return zig

