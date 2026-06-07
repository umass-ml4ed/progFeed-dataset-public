# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def funky(n):
    if n == 0:
        return 0
    if n > 0:
        return n + funky(n - 2)
    else:
        return -n + funky(n + 2)
