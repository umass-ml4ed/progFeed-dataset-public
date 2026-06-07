# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n > 0:
        count = 0
        numbas = range(2, int(n ** 0.5) + 1)
        while count < len(numbas):
            if n % numbas[count] == 0:
                return False
            count += 1
        return True
    return False

print(is_prime(7))
print(is_prime(4))
print(is_prime(-3))
print(is_prime(17))
