# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(strlist, n):
    count = 0
    for str in strlist:
        if len(str) >= n:
            count += 1
    return count