# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

def count_strings(lst:list,n:int):
    c=0
    for i in lst:
        if len(i)>=n:
            c+=1
    return c

count_strings(['', 'a', 'aa', 'aaa'], 0)   # should return 4
count_strings(['', 'a', 'aa', 'aaa'], 2)   # should return 2 
count_strings(['', 'a', 'aa', 'aaa'], 4)   # should return 0

