# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(list, n):
    count = 0
    for string in list:
        if len(string) >= n:
            count += 1
    return count
