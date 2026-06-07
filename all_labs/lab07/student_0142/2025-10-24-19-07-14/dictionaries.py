# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

#count_words

def count_words(words_tuple):
    word_count ={}
    for word in words_tuple:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

#average_prices

def average_prices(prices_tuple):
    total_price = {}
    count = {}
    
    for commodity, price in prices_tuple:
        if commodity in total_price:
            total_price[commodity] += price
            count[commodity] += 1
        else:
            total_price[commodity] = price
            count[commodity] = 1
    
    average_price = {}
    for commodity in total_price:
        average_price[commodity] = total_price[commodity] / count[commodity]
    
    return average_price

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))  

#count_bigrams

def count_bigrams(words):
    bigram_counts = {}
    for i in range(len(words)-1):
        bigram = (words[i],words[i+1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts

print(count_bigrams(()))
print(count_bigrams(('hello',)))  

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

