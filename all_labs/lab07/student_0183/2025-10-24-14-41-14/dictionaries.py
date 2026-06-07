# REDACTED_NAME
# REDACTED_EMAIL
# REDACTED_SPIRE_ID

def count_words(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
    else:
        word_counts[word] = 1
    
    return word_counts
    

def average_prices(prices):
    total = {}
    count = {}
    for item, price in prices:
        if item in total:
            total[item] += price
            count[item] += 1
        else:
            total[item] = price
            total[item] = 1

    avg = {}
    for item in total:
        avg[item] = round(total[item] / count[item], 1) 
    return avg


def count_bigrams(words):
    bigram_counts = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts

