def count_words(words):
    word_counts= {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] += 1
    return word_counts

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
    avg = {}
    for name in total:
        avg[name] = total[name] / count[name]
    return avg

def count_bigrams(words):
    bigrams = {}
    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        if pair in bigrams:
            bigrams[pair] += 1
        else:
            bigrams[pair] = 1
    return bigrams