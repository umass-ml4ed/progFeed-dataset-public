# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def count_words(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts

def average_prices(prices):
    totals = {}
    count = {}
    for name,price in prices:
        name=name.lower()
        if name in totals:
            totals[name] += price
            count[name]+= 1
        else:
            totals[name]=price
            count[name] = 1
    return {name: totals[name]/ count[name] for name in totals}

def count_bigrams(words):
    counts = {}
    for i in range(len(words) - 1):
        bg = (words[i], words[i + 1])
        counts[bg] = counts.get(bg, 0) + 1
    return counts