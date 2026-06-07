# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst, n):
    count = 0
    for i in lst:
        if len(i) >= n:
            count += 1
    return count
print(count_strings(['', 'a', 'aa', 'aaa'], 0))
        