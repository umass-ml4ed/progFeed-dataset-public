# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(str_list, n):
    counter = 0
    for strings in str_list:
        if len(strings) >= n:
            counter += 1
    return counter
