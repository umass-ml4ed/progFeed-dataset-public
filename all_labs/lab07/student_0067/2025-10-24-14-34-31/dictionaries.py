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
        
def count_bigrams(words):
    new_dict = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i+1])
        new_dict[bigram] = new_dict.get(bigram, 0) + 1
    return new_dict

