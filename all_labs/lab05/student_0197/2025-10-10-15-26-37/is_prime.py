# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
	i = 2
	while i <= (n**0.5):
		if (n % i) == 0:
			return False
		i+=1
	if n % (n**0.5) == 0:
		return False
	return True