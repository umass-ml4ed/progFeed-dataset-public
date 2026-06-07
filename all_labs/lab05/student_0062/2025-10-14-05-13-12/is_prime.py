# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n > 1:
        div = 2
        while div <= n ** 0.5:
            if n % div == 0:
                return(False)
            div += 1
        return(True)
    else:
        return(False)