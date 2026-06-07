# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    while n > 0:
        i = 0
        while i < n:
            print(n-i, end= " ")  
            i += 1
        print("\n")     
        n -= 1

def merge_dicts(d1, d2):
    new = d1.copy()
    for i in d2:
        if i in new:
            new[i] += d2[i]
        else:
            new[i] = d2[i]
    return new

