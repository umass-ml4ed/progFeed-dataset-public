
# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    word_counts = {}
    
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))   

test2 = ('apple', 'banana', 'apple', 'orange', 'banana', 'apple')
print(count_words(test2)) 

def average_prices(prices):
    total = {}   
    count = {}  

    for name, price in prices:
        if name in total:
            total[name] += price
            count[name] += 1
        else:
            total[name] = price
            count[name] = 1
    
    averages = {}
    for name in total:
        averages[name] = total[name] / count[name]
    
    return averages

def count_bigrams(words):
    bigram_counts = {}
    
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    
    return bigram_counts

