# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def average_prices(comm):
    counts = {}
    totals = {}
    for entry in comm:
        index, price = entry
        counts[index] = counts.get(index, 0) + 1
        totals[index] = totals.get(index, 0.0) + price
    avg_price = {}
    for index in totals:
        avg_price[index] = totals[index] / counts[index]
    return avg_price

def count_bigrams(words):
    bigram_dict = {}
    for word in words:
        current_word = words.index(word)
        second_word = words[current_word+1]
        bigram = (word, second_word)
        bigram_dict[bigram] = bigram_dict.get(bigram, 0) + 1
    return bigram_dict

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))