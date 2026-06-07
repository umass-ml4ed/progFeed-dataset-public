# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
import math

def count_strings(lst, n):
    count = 0
    for string in lst:
        if len(string) >= n:
            count += 1
    return count

