# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(string_list, n):
    count = 0
    for string in string_list:
        if len(string) >= n:
            count += 1
    return count