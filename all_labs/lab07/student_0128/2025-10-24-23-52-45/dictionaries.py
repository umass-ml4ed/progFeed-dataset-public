# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(a_tuple):
    return {word: a_tuple.count(word) for word in a_tuple}

def average_prices(commodities):
    beeg_dictionary = {}
    for tup in commodities:
        beeg_dictionary[tup[0]] = 0
    for tup in commodities:
        beeg_dictionary[tup[0]] += tup[1]
    for key in beeg_dictionary:
        beeg_dictionary[key] = beeg_dictionary[key] / list(item[0] for item in commodities).count(key)
    return beeg_dictionary

def count_bigrams(words):
    bigrams = list((words[index], words[index + 1]) for index in range(len(words) - 1))
    return {b: bigrams.count(b) for b in bigrams}