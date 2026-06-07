# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    return word_count


def average_prices(prices):
    total_price = {}
    total_number = {}

    for name, price in prices:
        if name in total_price:
            total_price[name] = total_price[name] + price
            total_number[name] = total_number[name] + 1
        else:
            total_price[name] = price
            total_number[name] = 1

    avg_price = {}

    for name in total_price:
        avg_price[name] = total_price[name] / total_number[name]

    return avg_price


def count_bigrams(words):
    bigram_number = {}

    if len(words) < 2:
        return bigram_number

    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_number:
            bigram_number[bigram] = bigram_number[bigram] + 1
        else:
            bigram_number[bigram] = 1

    return bigram_number

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))