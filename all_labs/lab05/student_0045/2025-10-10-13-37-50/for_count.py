# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(lst: list, n: int):
    total = 0
    if n <= 0 :
        return len(lst)
    for i in lst:
        if len(i)>=n:
            total+=1
    return total

print(count_strings(['', 'a', 'aa', 'aaa'], 0))   # should return 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))   # should return 2 
print(count_strings(['', 'a', 'aa', 'aaa'], 4))   # should return 0
  