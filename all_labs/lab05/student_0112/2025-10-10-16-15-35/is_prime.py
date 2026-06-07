# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def is_prime(n):
    i = 2
    count = 0
    while (i <= int(n**0.5)):
        if (n%i) == 0:
            count += 1
        i += 1
    if (count != 0):
        return False
    else:
        return True
print(is_prime(17))