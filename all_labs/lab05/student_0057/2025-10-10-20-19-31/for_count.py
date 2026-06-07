# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(list_of_strings, n):
    count = 0
    for s in list_of_strings:
       if len(s) >= n:
           count += 1
    return count
print(count_strings(['', 'a', 'aa', 'aaa'], 0))
print(count_strings(['', 'a', 'aa', 'aaa'], 2))
print(count_strings(['', 'a', 'aa', 'aaa'], 4))