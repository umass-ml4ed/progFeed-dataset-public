# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst : list , n : int) -> int:
    count = 0
    for i in range(len(lst)):
        if len(lst[i]) >= n:
            count += 1
    return count


