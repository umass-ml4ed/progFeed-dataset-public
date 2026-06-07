# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(strings, n):
    longs = 0
    for i in strings:
        if len(i) >= n:
            longs += 1
    return longs

print(count_strings(['', 'a', 'aa', 'aaa'], 0))
print(count_strings(['', 'a', 'aa', 'aaa'], 2))
print(count_strings(['', 'a', 'aa', 'aaa'], 4))