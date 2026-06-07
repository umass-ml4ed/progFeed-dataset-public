# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lis):
    if len(lis) <= 1:
        return lis(0)
    else:
        nex_lis = max_recursive(lis.remove(min(lis)))
        return nex_lis
max_recursive([3, 10, 2, 8, 6])     