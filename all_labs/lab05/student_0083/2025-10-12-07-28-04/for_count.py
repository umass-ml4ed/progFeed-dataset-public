# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst_str, n):
    count = 0
    for chr in lst_str:
        if len(chr) >= n:
            count += 1
    return count
