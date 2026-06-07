# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lis):
	if len(lis) == 0:
		return 0
	x = max_recursive(lis[1:])
	if lis[0] >= x:
		return lis[0]
	else:
		return x

def sum_lists_recursive(lis1, lis2):
	if len(lis1) == len(lis2) == None:
		return 0
	elif (len(lis1) == 1) and (len(lis2) == 1):
		return lis1[0] + lis2[0]
	else:
		#try:
		x = lis1[0] + lis2[0] + sum_lists_recursive(lis1[1:], lis2[1:])
		return x
		#except:
		#	x = lis1[0] + lis2[0]
		#	return x
		

def funky(n):
	if (n == 1) or (n == 0):
		return 1
	elif (n % 2) == 0:
		return 2 * funky(n//2)
	else:
		return 1 + 2 * funky(n+1)

def permutations(lst):
	if len(lst) == 1:
		return lst