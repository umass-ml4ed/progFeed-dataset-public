# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    counts = {}
    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    return counts

def average_prices(prices):
    total = {}
    count = {}
    for name, price in prices:
        total[name] = total.get(name, 0) + price
        count[name] = count.get(name, 0) + 1
    return {name: total[name] / count[name] for name in total}

def count_bigrams(words):
    counts = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        counts[bigram] = counts.get(bigram, 0) + 1
    return counts

if __name__ == "__main__":
    words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
    print(count_words(words))
    prices = (('a', 1.0), ('c', 4.2), ('b', 3.9),
              ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
    print(average_prices(prices))

    words2 = ('she', 'knows', 'and', 'she', 'knows', 'that',
              'he', 'knows', 'that', 'she', 'knows')
    print(count_bigrams(words2))