# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def is_prime(n):
    if n <= 1:
        return False

    i = 2
    while i <= int(n ** 0.5):
        if n % i == 0:
            # Found a divisor → not prime
            return False
        i += 1

    return True

some_string = 'How many vowels are there in this string?'
count = 0  # initialize the count variable

for char in some_string:
    if char.lower() in 'aeiou':   
        count += 1                

print('Number of vowels:', count)
