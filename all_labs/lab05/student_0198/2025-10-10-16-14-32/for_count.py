# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def count_strings(l: list, n: int):
    count = 0
    for ch in l:
        if len(ch) >= n:  # check length greater than or equal
            count += 1
            break  # stop after counting the first one
    print(count)

count_strings(["apple", "banana", "cherry"], 6)  # prints: 1
