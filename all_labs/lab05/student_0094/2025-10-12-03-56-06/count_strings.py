# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# for_count.py

def count_strings(strings, n):
    """Return how many strings in the list have length >= n."""
    count = 0
    for s in strings:           # <-- for loop as requested
        if len(s) >= n:
            count += 1
    return count

# quick checks
# print(count_strings(['', 'a', 'aa', 'aaa'], 0))  # 4
# print(count_strings(['', 'a', 'aa', 'aaa'], 2))  # 2
# print(count_strings(['', 'a', 'aa', 'aaa'], 4))  # 0

        
print (count_strings([' ', 'aaaaaaa', 'aaaaaaaa'], 4))
            