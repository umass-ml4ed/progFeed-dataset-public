# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_strings(strings, n):
    count=0
    for string in strings:
        if len(string)>=n:
            count=count+1
    return count
print(count_strings(['', 'a', 'aa', 'aaa'], 0))   # should return 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))   # should return 2 pcount_strings(['', 'a', 'aa', 'aaa'], 4))   # should return 0
