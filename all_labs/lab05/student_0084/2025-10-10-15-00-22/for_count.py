# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(l, n):
    count = 0
    for item in l:
        if len(item) >= n:
            count += 1
    return count

print(count_strings(['', 'a', 'aa', 'aaa'], 0))   # should return 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))   # should return 2 
print(count_strings(['', 'a', 'aa', 'aaa'], 4))   # should return 0