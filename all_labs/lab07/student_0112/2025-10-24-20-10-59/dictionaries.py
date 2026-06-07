# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def count_words(words):
    some_dict={}
    k=0
    for i in range (len(words)):
        if (words[i] not in some_dict):
            # some_dict[words[i]] = words[i]
            some_dict[words[i]] = 1
            k +=1
        else:
            some_dict[str(words[i])]+=1
    return some_dict

def average_prices(tup):
    result = {}
    counts = {}

    for item, price in tup:
        if item in result:
            result[item] += price
            counts[item] += 1
        else:
            result[item] = price
            counts[item] = 1
    for item in result:
        result[item] /= counts[item]

    return result


# prices = (('gouda cheese 1 lbs', 3.49), ('organic oyster mushroom 1 lbs', 6.89), ('toilet paper 1 roll', 3.99), ('apple juice 1 gallon', 7.99), ('gouda cheese 1 lbs', 4.29), ('toilet paper 1 roll', 4.19), ('talenti gelato vanilla', 5.59))
# print(average_prices(prices))
def count_bigrams(tup):
    if len(tup) <= 1:
        return {}
    bigram_counts = {}
    for i in range(len(tup) - 1):
        bigram = (tup[i], tup[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] =1


    return bigram_counts



words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))



