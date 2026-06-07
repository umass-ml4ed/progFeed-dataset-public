# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(strs, n):
    num_strings = 0
    for word in strs:
        if len(word) >= n:
            num_strings += 1
    return num_strings

print(count_strings(['', 'a', 'aa', 'aaa'], 0))   # should return 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))   # should return 2 
print(count_strings(['', 'a', 'aa', 'aaa'], 4))   # should return 0

