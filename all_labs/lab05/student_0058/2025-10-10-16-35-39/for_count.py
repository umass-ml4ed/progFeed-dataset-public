# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings (list,n):
    count = 0
    for s in list:
        if len(s) >= n:
            count += 1
    return count



print(count_strings(['', 'a', 'aa', 'aaa'], 0))   # Expected: 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))   # Expected: 2
print(count_strings(['', 'a', 'aa', 'aaa'], 4))