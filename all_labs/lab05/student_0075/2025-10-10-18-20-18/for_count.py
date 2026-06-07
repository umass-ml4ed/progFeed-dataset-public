# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(strings, n):
    c = 0
    for s in strings:
        if len(s) >= n:
            c += 1
    return c

print(count_strings(['', 'a', 'aa', 'aaa'], 0))   # should return 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))   # should return 2 
print(count_strings(['', 'a', 'aa', 'aaa'], 4))   # should return 0
