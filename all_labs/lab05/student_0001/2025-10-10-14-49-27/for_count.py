# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lis, n):
    count = 0
    for l in lis:
        if len(l) >= n:
            count += 1
    return count

count_strings(['', 'a', 'aa', 'aaa'], 0)