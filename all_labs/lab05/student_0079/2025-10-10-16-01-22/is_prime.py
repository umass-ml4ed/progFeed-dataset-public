# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n == 2:
        return True
    elif n > 1:
        for count in range(2, int(n**0.5) + 1):
            if n % count == 0:
                return False
            else:
                if count == int(n**0.5):
                    return True
    else:
        return False
    '''
    count = 2
    prime = True
    while n % count != 0 and count <= int(n**0.5):
        if count == int(n**0.05):
            prime = False
        count += 1
    return prime
    '''

print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(4))
print(is_prime(15))
print(is_prime(17))
print(is_prime(25))
print(is_prime(26))
print(is_prime(97))

print(is_prime(2))  # Expected output: True
print(is_prime(4))  # Expected output: False
print(is_prime(5))  # Expected output: True
print(is_prime(9))  # Expected output: False
print(is_prime(16)) # Expected output: False
print(is_prime(19)) # Expected output: True