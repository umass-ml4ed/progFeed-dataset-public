# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * funky(n // 2)
    else:
        return 1 + 2 * funky(n + 1)

