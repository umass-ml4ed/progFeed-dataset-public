# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_prime(num):
    result = True
    for val in range(2, int(num**0.5) + 1):
        if num % val == 0:
            result = False
            break
        else:
            result = True
            continue
    return result
print(is_prime(4))