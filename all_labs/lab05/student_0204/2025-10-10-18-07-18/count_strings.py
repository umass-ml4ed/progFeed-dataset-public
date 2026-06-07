# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(list, n):
    count = 0
    for x in range(len(list)):
        if len(list[x]) >= n:
            count += 1
    return count
