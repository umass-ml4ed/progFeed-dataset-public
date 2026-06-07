# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_strings(l:list, n:int):
    num = 0
    for char in l:
        count = len(char)
        if count >= n:
            num += 1
    return num

count_strings(['', 'a', 'aa', 'aaa'], 0)   # should return 4
count_strings(['', 'a', 'aa', 'aaa'], 2)   # should return 2 
count_strings(['', 'a', 'aa', 'aaa'], 4)   # should return 0

