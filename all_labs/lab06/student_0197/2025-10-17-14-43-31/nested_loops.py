# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first, last):
	full = []
	for j in first:
		for i in last:
			full.append(j+" "+i)
	return full

def average_scores(scores):
	Average = []
	for j in scores:
		temp = []
		for i in range(len(j)):
			if j[i][1] == 0:
				temp.append(j[i][0])
			elif j[i][1] == 1:
				temp.append((j[i][0] * 0.9))
			elif j[i][1] == 2:
				temp.append((j[i][0] * 0.75))
			elif j[i][1] == 3:
				temp.append((j[i][0] * 0.50))
			elif j[i][1] >= 4:
				temp.append(0)
		Temp_av = 0
		for c in temp:
			Temp_av += c
		Average.append(Temp_av / len(temp))
	return Average

#print(average_scores([[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]))