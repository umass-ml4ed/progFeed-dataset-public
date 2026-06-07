# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED
counted_words = {}
def count_words(a):
    counted_words = {}
    for x in a:
        if x not in counted_words:
            counted_words[x] = 1
        else:
            counted_words[x] = counted_words[x] + 1
    return (counted_words)

def average_prices(a):
    prices = {}
    times = {}
    for x in a:
        if x[0] not in times:
            times [x[0]] = 1
            prices [x[0]] = x[1]
        else:
            times[x[0]] = times[x[0]] + 1
            prices [x[0]] = prices [x[0]] + x[1] 
    for x in prices:
        prices[x] = prices[x]/times[x]
    return (prices)

def count_bigrams(a):
    bigram_count = {}
    if len(a) = 1:
        return bigram_count
    for x in range (0,len(a) - 1):
        if f"{a[x]}, {a[x+1]}" not in bigram_count:
            bigram_count[f"{a[x]}, {a[x+1]}"] = 1
        else:
            bigram_count[f"{a[x]}, {a[x+1]}"] += 1
    return bigram_count
