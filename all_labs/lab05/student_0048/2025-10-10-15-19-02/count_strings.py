# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(lis, n):
    count = 0
    for i in lis:
            if len(i) >= n:
                count = count + 1 
    return count

print(count_strings(['', 'a', 'aa', 'aaa'], 0))
print(count_strings(['', 'a', 'aa', 'aaa'], 2))
print(count_strings(['', 'a', 'aa', 'aaa'], 4))

