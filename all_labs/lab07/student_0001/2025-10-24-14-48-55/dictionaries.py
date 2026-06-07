# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    dict = {}
    for w in words:
        if w not in dict:
            dict[w] = 1
        else:
            dict[w] += 1
    return dict

# words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
# print(count_words(words))

def average_prices(data):
    total = {}
    count = {}

    for name, price in data:
        if name in total:
            total[name] += price
            count[name] += 1
        else:
            total[name] = price
            count[name] = 1

    average = {}
    for name in total:
        average[name] = total[name] / count[name]

    return average

# prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
# print(average_prices(prices))

def count_bigrams(words):
    bigram_counts = {}

    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1

    return bigram_counts

# words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
# print(count_bigrams(words))