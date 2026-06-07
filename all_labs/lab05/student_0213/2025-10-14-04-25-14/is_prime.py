# Name     : REDACTED_NAME
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    i = 2
    if n == 2:
        return True
    while i - 1 < n**0.5:
        if n%i == 0:
            return False
        elif i >= n**0.5 and n%i != 0:
            return True
        else:
            i += 1
            continue
        
