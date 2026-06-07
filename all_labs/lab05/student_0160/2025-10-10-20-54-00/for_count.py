# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lis:list, n:int):
    count = 0
    for string in lis:
        if len(string) >= int(n):
            count+=1
    return print(count)
    
count_strings(['', 'a', 'aa', 'aaa'], 0)   # should return 4
count_strings(['', 'a', 'aa', 'aaa'], 2)   # should return 2 
count_strings(['', 'a', 'aa', 'aaa'], 4)
