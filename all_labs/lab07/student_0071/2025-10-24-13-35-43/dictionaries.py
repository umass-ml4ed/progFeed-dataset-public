# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def count_words (words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count [word] = 1
    return word_count

def average_prices (commodities):
    total_prices = {}
    count = {}
    for commidity, price in commodities:
        if commidity in total_prices:
            total_prices[commidity] += price
            count [commidity] += 1
        else:
            total_prices[commidity] = price
            count [commidity] = 1
    average_dict = {}  
    for commidity in total_prices:
        average_dict[commidity] = total_prices[commidity] / count[commidity]
    return average_dict

def count_bigrams(words):
    bigram_counts = {}
    for i in range(len(words)- 1):
        bigram = (words[i], words [i+1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram]= 1
    return bigram_counts