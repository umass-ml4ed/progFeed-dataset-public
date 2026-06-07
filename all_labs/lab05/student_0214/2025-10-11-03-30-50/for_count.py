# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def count_strings(lst, n):
    count = 0
    for strs in lst:
        if len(strs) >= n:
            count += 1
        else:
            continue
    return count

