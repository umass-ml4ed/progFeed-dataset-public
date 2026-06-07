def count_words(words):
    some_dict = {}
    for letters in words:
        if letters in some_dict:
            some_dict[letters]+=1
        else:
            some_dict[letters]=1
    return some_dict



words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw','mayur','mayur')
print(count_words(words))


def average_prices(items):
    totals = {}
    counts = {}
    
    for name, price in items:
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



prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

items=(('gouda cheese 1 lbs', 3.49), ('organic oyster mushroom 1 lbs', 6.89), ('toilet paper 1 roll', 3.99), ('apple juice 1 gallon', 7.99), ('gouda cheese 1 lbs', 4.29), ('toilet paper 1 roll', 4.19), ('talenti gelato vanilla', 5.59))


def count_bigrams(words):
    bigram_dict = {}
    
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_dict:
            bigram_dict[bigram] += 1
        else:
            bigram_dict[bigram] = 1
    
    return bigram_dict

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))