# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def count_words(tup):
    some_dict = {}
    for word in tup:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word] = 1
    return some_dict

def average_prices(tup):
    price_dict = {}
    number_dict = {}
    average_dict = {}
    for item in tup:
        if item[0] not in price_dict:
            number_dict[item[0]] = 1
            price_dict[item[0]] = item[1]
        else:
            number_dict[item[0]] += 1
            price_dict[item[0]] += item[1]
    for good in price_dict:
        average_dict[good] = (price_dict[good] / number_dict[good])
    return average_dict

def count_bigrams(tup):
    some_dict = {}
    n = 1
    for word in tup[:len(tup) - 1]:
        bigram = (word, tup[n])
        if bigram not in some_dict:
            some_dict[bigram] = 1
            n += 1
        else:
            some_dict[bigram] += 1
            n += 1
    return some_dict
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

