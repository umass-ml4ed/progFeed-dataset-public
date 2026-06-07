# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    word_count = {}

    for c in words:
        word_count[c] = word_count.get(c, 0) + 1

    return word_count

def average_prices(commodities):
    new_dict = {}

    for c in commodities:
        thing, value = c
        if thing in new_dict:
            new_dict[thing] = round((new_dict[thing] + value )/ 2, 1)
        else:
            new_dict[thing] = value
    return new_dict
        
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
# print(average_prices(prices))
print(average_prices(prices))