# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1 
    return word_counts

something = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(something))

def average_prices(data):
    total = {}
    count = {} 
    for item, price in data: 
        if item not in total:
            total[item] = price
            count[item] = 1
        else: 
            total[item] += price
            count[item] += 1
    averages = {}
    for item in total:
        averages[item] = total[item] / count[item] 
    return averages

def count_bigrams(words):
    bigrams = {} 
    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        if pair not in bigrams:
            bigrams[pair] = 1
        else: 
            bigrams[pair] += 1
    return bigrams
