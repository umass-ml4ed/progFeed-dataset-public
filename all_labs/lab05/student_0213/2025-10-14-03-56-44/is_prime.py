# Name     : REDACTED_NAME
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    i = 2
    while i<=n**0.5:
        if n%i == 0:
            return False
        else:
            i += 1
            continue
    while i + 1 >= n**0.5:
        if n == 1:
            return False
        if n%i != 0:
            return True
        else:
            return False
        
print(is_prime(1))