# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def is_prime(n):
    i = 2
    count = 0
    while (i <= n**1/2):
        if (n%i) == 0:
            count += 1
        i += 1
    if (count != 0):
        return False
    else:
        return True

