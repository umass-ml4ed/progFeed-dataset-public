# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
	if n <= 1:
		return True
	for i in range(2, n // 2):
		if n % i == 0:
			return False
	return True
print(is_prime(36))
