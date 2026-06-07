# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words: tuple) -> dict:
    freqs = {}
    for w in words:
        if w in freqs:
            freqs[w] += 1
        else:
            freqs[w] = 1
    return freqs


def average_prices(price_tuples: tuple) -> dict:
    totals = {}
    counts = {}
    for name, price in price_tuples:
        if name in totals:
            totals[name] += price
            counts[name] += 1
        else:
            totals[name] = price
            counts[name] = 1
    averages = {}
    for name in totals:
        averages[name] = totals[name] / counts[name]
    return averages


def count_bigrams(words: tuple) -> dict:
    bigram_counts = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts


if __name__ == "__main__":
    words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
    print(count_words(words))  

    print(count_words(()))  
    print(count_words(('hello',)))  
    prices = (
        ('gouda cheese 1 lbs', 3.49),
        ('organic oyster mushroom 1 lbs', 6.89),
        ('toilet paper 1 roll', 3.99),
        ('apple juice 1 gallon', 7.99),
        ('gouda cheese 1 lbs', 4.29),
        ('toilet paper 1 roll', 4.19),
        ('talenti gelato vanilla', 5.59),
    )
    print(average_prices(prices))
    simple_prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
    print(average_prices(simple_prices)) 

    print(count_bigrams(()))  
    print(count_bigrams(('hello',)))  
    words2 = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
    print(count_bigrams(words2))


