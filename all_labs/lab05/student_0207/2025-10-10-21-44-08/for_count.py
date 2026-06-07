# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(list,n):
    i=0
    for item in list:
       if n <= len(item):
           i += 1
    return i

print(count_strings(['', 'a', 'aa', 'aaa'], 0))  # should return 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))  # should return 2 
print(count_strings(['', 'a', 'aa', 'aaa'], 4))  # should return 0

