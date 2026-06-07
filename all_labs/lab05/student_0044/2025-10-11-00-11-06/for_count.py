# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(a, n):
    count = 0
    for i in a:
        if len(i) >= n:
            count += 1
    return count 
#print(count_strings(['', 'a', 'aa', 'aaa'], 0))   # should return 4
#print(count_strings(['', 'a', 'aa', 'aaa'], 2))   # should return 2 
#print(count_strings(['', 'a', 'aa', 'aaa'], 4)) 