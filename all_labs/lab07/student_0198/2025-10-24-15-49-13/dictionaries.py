# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def count_words(tup: tuple):
    some_dict = {}
    for ch in tup:
        if ch in some_dict:
            some_dict[ch] += 1
        else:
            some_dict[ch] = 1
    return some_dict
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')

def average_prices(tup: tuple):
    dic_1 = {}
    unique_names = set(name for name, _ in tup)
    
    for name in unique_names:
        prices = [price for n, price in tup if n == name]
        dic_1[name] = sum(prices) / len(prices)
    
    return dic_1


def count_bigrams(tup: tuple):
    some_dict = {}
    for i in range(len(tup) - 1):
        bigram = (tup[i], tup[i + 1])
        if bigram in some_dict:
            some_dict[bigram] += 1
        else:
            some_dict[bigram] = 1
    return some_dict
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))
