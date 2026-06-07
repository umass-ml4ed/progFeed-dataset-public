# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(words_tuple):
    words = {} 

    for word in words_tuple:
        if word in words:
           words[word] += 1  
        else:
            words[word] = 1   

    return words


words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))


def average_prices(prices_tuple):
    total_prices = {}  
    counts = {}       

    for commodity, price in prices_tuple:
        if commodity in total_prices:
            total_prices[commodity] += price
            counts[commodity] += 1
        else:
            total_prices[commodity] = price
            counts[commodity] = 1

    averages = {}
    for commodity in total_prices:
        averages[commodity] = total_prices[commodity] / counts[commodity]

    return averages
prices = (
    ('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8)
)

print(average_prices(prices))


def count_bigrams(words):
    sentence = {}

    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])  # form a tuple of two consecutive words
        
        # increment count or initialize if new
        if bigram in sentence:
            sentence[bigram] += 1
        else:
            sentence[bigram] = 1
    
    return sentence

count_bigrams(())         
count_bigrams(('hello',))

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))