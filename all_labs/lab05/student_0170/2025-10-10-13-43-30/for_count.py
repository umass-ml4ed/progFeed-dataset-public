# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(list,n):
    res = 0
    for s in list:
        if len(s) >= n:
            res += 1
    return res

print(count_strings([],0))