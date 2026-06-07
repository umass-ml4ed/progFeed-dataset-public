# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_zigzag(l):
	if len(l) < 3:
		return True

	if len(l) < 3:
		return True

	sum = 0
	for a, b, c in zip(l, l[1:], l[2:]):
		
		if not ((b > a and b > c) or (b < a and b < c)):
			sum += 1
	return sum == 0
