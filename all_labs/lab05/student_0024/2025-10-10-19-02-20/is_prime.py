def is_prime(num):
    num = int(num)
    if num < 2:
        return "The number is not a prime number"
    for count in range(2, int(num**0.5) + 1):
        if num % count == 0:
            return "The number is not a prime number"
    return "The number is prime"
def is_prime(num):
    num = int(num)
    if num <= 1:
        return "The number is not a prime number"
    i = 2
    while i <= int(num**0.5):
        if num % i == 0:
            return "The number is not a prime number"
        i += 1
    return "The number is prime"
