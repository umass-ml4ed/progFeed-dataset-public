# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(L,n):
    count=0
    for i in L:
        if len(i)>=n:
            count+=1
    return count
print(count_strings(['', 'a', 'aa', 'aaa'], 4))