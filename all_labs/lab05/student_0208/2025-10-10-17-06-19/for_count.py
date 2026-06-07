# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(l,n):
    count=0
    for s in l:
        if len(s)>=n:
            count+=1
    return count

