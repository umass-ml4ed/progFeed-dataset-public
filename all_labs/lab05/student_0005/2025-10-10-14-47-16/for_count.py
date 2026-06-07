# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst, n):
    num = 0
    for str in lst:
        if len(str) >= n:
            num += 1
    return num

# print(count_strings(['', 'a', 'aa', 'aaa'], 0))
# print(count_strings(['', 'a', 'aa', 'aaa'], 2))
# print(count_strings(['', 'a', 'aa', 'aaa'], 4))