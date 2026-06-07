# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def average_prices(prices):
    totals = {}
    counts = {}
    for item, price in prices:
        if item in totals:
            totals[item] += price
            counts[item] += 1
        else:
            totals[item] = price
            counts[item] = 1
    averages = {}
    for item in totals:
        averages[item] = round(totals[item] / counts[item], 1)
    return averages


def count_bigrams(words):
    bigram_count = {}
    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        if pair in bigram_count:
            bigram_count[pair] += 1
        else:
            bigram_count[pair] = 1
    return bigram_count



# Test for count_words
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))  # {'he': 1, 'saw': 4, 'a': 2}

# Test for average_prices
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2),
            ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))  # {'a': 1.1, 'c': 4.2, 'b': 4.0, 'd': 10.4}

# Test for count_bigrams
words2 = ('she', 'knows', 'and', 'she', 'knows', 'that',
            'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words2))

