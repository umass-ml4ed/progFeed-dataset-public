# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lis):
	#n = 1
	if len(lis) < 3:
		return True
	for i in range(1,(len(lis)-1)):
		if (lis[i] < lis[i-1]) and (lis[i] < lis[i+1]):
			pass
		elif (lis[i] > lis[i-1]) and (lis[i] > lis[i+1]):
			pass
		else:
			return False
		#n+=1
	return True

#	while i < (len(lis)-1):
#		if (lis[i] < lis[i-1]) and (lis[i] < lis[i+1]):
#			pass
#		elif (lis[i] > lis[i-1]) and (lis[i] > lis[i+1]):
#			pass
#		else:
#			return False
#		i+=1
#	return True

