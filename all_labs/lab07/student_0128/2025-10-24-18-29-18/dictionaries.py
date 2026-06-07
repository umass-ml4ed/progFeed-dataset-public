# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(a_tuple):
    return {word: a_tuple.count(word) for word in set(a_tuple)}

def average_prices(commodities):
    beeg_dictionary = {}
    #return {item[0]: sum(list(thing[1] for thing in commodities if thing[0] == item)) / len(list(thing[0] for thing in commodities if thing[0] == item)) for item in set((stuff[0] for stuff in commodities))}
    
    for tup in set(commodities):
        beeg_dictionary[tup[0]] = 0
    for tup in commodities:
        beeg_dictionary[tup[0]] += tup[1]
    for key in beeg_dictionary:
        beeg_dictionary[key] = beeg_dictionary[key] / list(item[0] for item in commodities).count(key)
    return beeg_dictionary