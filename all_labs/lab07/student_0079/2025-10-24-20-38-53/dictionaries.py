# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tuple):
	some_dict = {}
	count = 0
	for elem in tuple:
		if elem in tuple[:count]:
			some_dict[elem] = some_dict[elem] + 1
		else:
			some_dict[elem] = 1
		count += 1
	return some_dict

words = ('he', 'look', 'at', 'look', 'look', 'at', 'look')

print(count_words(words))

def average_prices(tuple):
	list = []
	dict_price = {}
	dict_number = {}
	dict_final = {}
	for elem in prices:
		if elem[0] in list:
			dict_price[elem[0]] = dict_price[elem[0]] + elem[1]
			dict_number[elem[0]] = dict_number[elem[0]] + 1
		else:
			dict_price[elem[0]] = elem[1]
			dict_number[elem[0]] = 1
	for key in dict_price:
		dict_final[key] = dict_price[key] / dict_number[key]
	return dict_final

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(tuple):
	bigram_count = {}
	if len(tuple) < 2:
		return bigram_count
	for elem in range(len(tuple) - 1):
		bigram = (tuple[elem], tuple[elem + 1])
		if bigram in bigram_count:
			bigram_count[bigram] = bigram_count[bigram] + 1
		else:
			bigram_count[bigram] = 1
	return bigram_count

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))