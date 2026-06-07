# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(a_tuple):
    return {word: a_tuple.count(word) for word in set(a_tuple)}

def average_prices(commodities):
    return {item[0]: sum((thing[1] for thing in commodities if thing[0] == item)) / len(list(thing[0] for thing in commodities if thing[0] == item)) for item in set((stuff[0] for stuff in commodities))}