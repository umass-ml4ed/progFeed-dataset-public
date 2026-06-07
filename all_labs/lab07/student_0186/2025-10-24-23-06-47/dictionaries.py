def count_words(words):
    some_dict = {}

    for w in words:
        if w in some_dict:
            some_dict[w] += 1
        else:
            some_dict[w] = 1

    return some_dict


def average_prices(prices):
    total = {}
    count = {}

    for name, val in prices:
        if name in total:
            total[name] += val
            count[name] += 1
        else:
            total[name] = val
            count[name] = 1

    averages = {}
    for name in total:
        averages[name] = total[name] / count[name]

    return averages

def count_bigrams(words):
    bigram_counts = {}


    if len(words) < 2:
        return bigram_counts


    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])

        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1

    return bigram_counts



