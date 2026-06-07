# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst, n):
    count = 0
    for i in range(len(lst)):
        if (len(lst[i]) >= n):
            count = count + 1
        else:
            count = count
    return count