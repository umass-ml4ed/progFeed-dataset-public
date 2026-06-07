# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def max_recursive(lst):
    if len(lst)==0:
        return 0
    if len(lst)==1:
        return lst[0]
    else:
        max_recursive_value = max_recursive(lst[1:])