# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


#n = int(input("Enter n_"))


def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= int(n**0.5):
        if n % i ==0:
            return False
        i += 1
    else:
        return True

print(is_prime(5))