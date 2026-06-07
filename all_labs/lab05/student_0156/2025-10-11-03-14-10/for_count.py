# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(list,n):
    count = 0
    for item in list:
        if len(item)>=n:
            count += 1
    return count

#count_strings(['', 'a', 'aa', 'aaa'], 0)   # should return 4
#count_strings(['', 'a', 'aa', 'aaa'], 2)   # should return 2 
#count_strings(['', 'a', 'aa', 'aaa'], 4)   # should return 0
