# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words_tuple):

    word_count = {}

    for word in words_tuple:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1

    return word_count

def average_prices(prices_tuple):

    total_price = {}
    counts = {}

    for commodity, price in prices_tuple:
        if commodity in total_price:
            total_price[commodity] += price
            counts[commodity] += 1
        else:
            total_price[commodity] = price
            counts[commodity] = 1

    averages = {}
    for commodity in total_price:
        averages[commodity] = total_price[commodity] / counts[commodity]

    return averages

def count_bigrams(words):

    if len(words) < 2:
        return {}
    
    bigrams_count = {}

    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])

        if bigram in bigrams_count:
            bigrams_count[bigram] += 1
        else:
            bigrams_count[bigram] = 1

    return bigrams_count


words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))



