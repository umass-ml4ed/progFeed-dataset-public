# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst, n):
    count = 0
    for s in lst:
        if len(s) >= n:
            count += 1
    return count

# Test cases
print(count_strings(['', 'a', 'aa', 'aaa'], 0))  # Expected: 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))  # Expected: 2
print(count_strings(['', 'a', 'aa', 'aaa'], 4))  # Expected: 0
