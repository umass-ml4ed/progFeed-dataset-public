# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(l, n):
    string_count = 0
    for string in l:
        if len(string) >= n:
            string_count += 1
    return string_count
