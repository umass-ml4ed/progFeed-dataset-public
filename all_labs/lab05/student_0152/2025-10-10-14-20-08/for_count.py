# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(list, n):
    s = 0
    for i in list:
        if len(i) >= n:
            s += 1
    return s

print(count_strings(['', 'a', 'aa', 'aaa'], 0))
print(count_strings(['', 'a', 'aa', 'aaa'], 2))
print(count_strings(['', 'a', 'aa', 'aaa'], 4))