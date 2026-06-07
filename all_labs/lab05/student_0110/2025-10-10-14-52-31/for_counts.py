# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_strings(lis_strings, n):
    count = 0
    for word in lis_strings:
        if len(word) >= n:
            count += 1
    return count

print(count_strings(['', 'a', 'aa', 'aaa'], 0))
print(count_strings(['', 'a', 'aa', 'aaa'], 2))
print(count_strings(['', 'a', 'aa', 'aaa'], 4))