# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(string_list, n):
    count = 0
    for s in string_list:
        if len(s) > n:
            count += 1
    return count
