def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def average_prices(prices):
    sums = {}
    counts = {}
    for item, price in prices:
        if item in sums:
            sums[item] += price
            counts[item] += 1
        else:
            sums[item] = price
            counts[item] = 1
    averages = {}
    for item in sums:
        averages[item] = sums[item] / counts[item]
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
