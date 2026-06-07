# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def max_recursive(lst):
    if len(lst)==0:
        return 0
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = max_recursive(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest

