# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count 

def average_prices(total_price):
    total = {}
    for x, y in total_price:
        if x not in total:
            total[x] = [y, 1]
        else:
            total[x][0] += y
            total[x][1] += 1
    averages = {}
    for x, y in total.items():
        average = y[0] / y[1]
        averages[x] = average
    return averages  

def count_bigrams(words):
    bigram_counts = {}
    for i in range(len(words) - 1):
        current_bigram = (words[i], words[i+1])
        if current_bigram in bigram_counts: 
            bigram_counts[current_bigram] += 1
        else:
            bigram_counts[current_bigram] = 1
    return bigram_counts

            
