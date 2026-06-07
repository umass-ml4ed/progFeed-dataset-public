# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))    

def average_prices(prices):
    totals = {}
    counts = {}
    for name, price in prices:
        totals[name] = totals.get(name, 0) + price
        counts[name] = counts.get(name, 0) + 1
    averages = {name: totals[name]/ counts[name] for name in totals}
    return averages
prices = (
    ('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8)
)    
#print(average_prices(prices))

def count_bigrams(words):
    bigram_counts = {}
    if len(words) < 2:
        return {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        bigram_counts[bigram] = bigram_counts.get(bigram, 0) + 1
    return bigram_counts
#print(count_bigrams(()))
#print(count_bigrams(('hello',)))
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows',)
print(count_bigrams(words))
    
            
