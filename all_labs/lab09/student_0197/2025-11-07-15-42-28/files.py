# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
	fileCur = open("stars_" + str(n) + ".txt", 'w')
	for i in range(n):
		fileCur.write((" "*(n-i-1)) + ("*" + "*"*(2*i)) + "\n")
	fileCur.close()	


def calc_avg_from_file():
	with ("grades.txt", 'r') as file:
		data = file.read()
		points = data.split('\n')
		avg = 0
		for i in points:
			avg += float(i)
		avg = avg / len(points)
		return avg