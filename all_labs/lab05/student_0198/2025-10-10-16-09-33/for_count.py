# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def count_strings(l:list, n:int):
    count=0
    for ch in l:
        if len(ch) >= n:
            count+=1
    print(count)
