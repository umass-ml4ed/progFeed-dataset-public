# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
	lines = []
	for start in range(n, 0, -1):
		line = ' '.join(str(i) for i in range(start, 0, -1))
		lines.append(line + "\n")
	return ''.join(lines)
		

def merge_dicts(d1, d2):
	result = {}
	for k, v in d1.items():
		result[k] = v
	for k, v in d2.items():
		if k in result:
			result[k] = result[k] + v
		else:
			result[k] = v
	return result

