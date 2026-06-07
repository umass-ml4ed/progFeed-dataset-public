# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(Tup):
	Dict = {}
	for i in Tup:
		if i in Dict:
			Dict[i] += 1
		else:
			Dict[i] = 1
	return Dict

#words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))

def average_prices(Tups):
	Dict = {}
	Total_Dict = {}
	Number_Dict = {}
	Index = []
	for i in Tups:
		if i[0] in Total_Dict:
			Total_Dict[i[0]] += 1
		else:
			Total_Dict[i[0]] = 1
		if i[0] in Number_Dict:
			Number_Dict[i[0]].append(i[1])
		else:
			Number_Dict[i[0]] = []
			Number_Dict[i[0]].append(i[1])
			Index.append(i[0])
	for i in Index:
		Dict[i] = sum(Number_Dict[i]) / Total_Dict[i] 
	#print(Index)
	#print(Total_Dict)
	#print(Number_Dict)
	return Dict

#prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
#print(average_prices(prices))

def count_bigrams(Tup):
	Dict = {}
	i = 0
	while i < (len(Tup) - 1):
		if (Tup[i],Tup[i+1]) in Dict:
			Dict[(Tup[i],Tup[i+1])] += 1
		else:
			Dict[(Tup[i],Tup[i+1])] = 1
		i += 1
	return Dict

#count_bigrams(())         # returns {}
#count_bigrams(('hello',)) # returns {} (note the trailing comma, which indicates
                          # this is a 1-element tuple instead of just a string)
#words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
#print(count_bigrams(words))
