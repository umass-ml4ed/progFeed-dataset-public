# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lis, n):
    x=0
    for i in lis:
        if len(i) >= n:
            x+=1
    return x

print(count_strings(['', 'a', 'aa', 'aaa'], 0))  # should return 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))   # should return 2 
print(count_strings(['', 'a', 'aa', 'aaa'], 4))  # should return 0

