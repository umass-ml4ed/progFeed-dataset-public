# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts

def average_prices(prices):
    sums, counts = {}, {}
    for k, p in prices:
        sums[k] = sums.get(k, 0.0) + float(p)
        counts[k] = counts.get(k, 0) + 1
    return {k: sums[k] / counts[k] for k in sums}

def count_bigrams(words):
    bigrams = {}
    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        bigrams[pair] = bigrams.get(pair, 0) + 1
    return bigrams
