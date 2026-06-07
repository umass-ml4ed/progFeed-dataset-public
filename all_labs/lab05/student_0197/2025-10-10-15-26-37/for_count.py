# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lis, x):
	n = 0
	for i in lis:
		if len(i) >= x:
			n+=1
	return n

