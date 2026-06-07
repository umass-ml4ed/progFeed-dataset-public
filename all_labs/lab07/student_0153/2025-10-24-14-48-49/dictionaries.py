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

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(prices):
    totals = {}
    counts = {}
    for tag, price in prices:
        if tag in totals:
            totals[tag] += price
            counts[tag] += 1
        else:
            totals[tag] = price
            counts[tag] = 1
    averages = {}
    for tag in totals:
        averages[tag] = totals[tag] / counts[tag]
    return averages
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))
    

def count_bigrams(tup):
    bigram_dict = {}
    for i in range(len(tup) - 1):
        bigram = (tup[i] , tup[i + 1])
        if bigram in bigram_dict:
            bigram_dict[bigram] += 1
        else:
            bigram_dict[bigram] = 1
    return bigram_dict
print(count_bigrams(()))
print(count_bigrams(('hello',)))
print(count_bigrams(('a', 'b', 'c')))
print(count_bigrams(('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')))
