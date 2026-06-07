# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(a, n):
    count = 0 
    for i in a : 
        b = len(i)
        if b >= n: 
            count += 1
    return count


