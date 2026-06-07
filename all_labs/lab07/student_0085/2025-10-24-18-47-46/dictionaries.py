# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


from unicodedata import name


def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
words = ("he", "saw", "a", "saw", "saw", "a", "saw")
print(count_words(words))


def average_prices(prices):
    totals = {}
    counts = {}
    for name, price in prices:
        if name in totals:
            totals[name] += price
            counts[name] += 1
        else:
            totals[name] = price
            counts[name] = 1
    averages = {}
    for name in totals:
        averages[name] = totals[name] / counts[name]
    return averages
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))



def count_bigrams(words):
    bigram_counts = {} 
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts
print(count_bigrams(()))
print(count_bigrams(('hello',)))
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))


