# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def count_strings(l: list, n: int):
    count=0
    for str in l:
        if len(str)>=n:
            count +=1
    return count
print(count_strings(['', 'a', 'aa', 'aaa'], 4))