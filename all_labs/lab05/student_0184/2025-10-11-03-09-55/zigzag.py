# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
import math

def is_zigzag(lst):
    for i in range(1, len(lst) - 1):
        bigger = lst[i] > lst[i-1] and lst[i] > lst[i+1]
        smaller = lst[i] < lst[i-1] and lst[i] < lst[i+1]

        if not (bigger or smaller):
            return False

    return True