# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
import math
import random
def max_recursive(lst):
    if len(lst)==1:
        return lst[0]
    max=max_recursive(lst[1:])
    if lst[0]>max:
        return lst[0]
    else:
        return max