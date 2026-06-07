# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_words(lst):
    counts = {}
    for word in lst:
        counts[word] = lst.count(word)
    return counts
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')


def average_prices(basket):
    prices = {}
    counts = {}
    for name, price in basket:
        prices[name] = prices.get(name, 0) + price
        counts[name] = counts.get(name, 0) + 1
    return {name: prices[name]/ counts[name] for name in prices}
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))

        
def count_bigrams(words):
    big = {}
    for i in range(len(words)-1):
        bigram = words[i], words[i + 1]
        if bigram in big:
            big[bigram] += 1
        else:
            big[bigram] = 1
    return big 



       
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))



       



        