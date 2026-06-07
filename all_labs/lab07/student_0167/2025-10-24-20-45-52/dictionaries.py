# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tuple_of_words):
    some_dict = {}
    for i in tuple_of_words:
        if i not in some_dict:
            some_dict[i] = 1
        else:
            some_dict[i] += 1 
    return some_dict

def average_prices(items: tuple) -> dict:
    sums = {}
    counts = {}

    for name, price in items:
        if name in sums:
            sums[name] += price
            counts[name] += 1
        else:
            sums[name] = price
            counts[name] = 1

    return {name: sums[name] / counts[name] for name in sums}


def count_bigrams(tuple_of_words):
    another_dict = {}
    n = len(tuple_of_words)
    for index in range(n - 1):
        first = tuple_of_words[index]
        second = tuple_of_words[index + 1]
        bigram = (first, second)
        another_dict[bigram] = another_dict.get(bigram, 0) + 1
    return another_dict

