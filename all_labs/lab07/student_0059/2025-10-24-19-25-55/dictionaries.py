# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(x):
    some_dict = {}
    for i in x:
        if i not in some_dict:
            some_dict[i] = 1
        else:
            some_dict[i] += 1
    return some_dict

print(count_words(x = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')))

def average_prices(x):
    total_price = {}
    total_number = {}
    for comm, price in x:
        if comm not in total_price:
            total_price[comm] = price
            total_number[comm] = 1
        else:
            total_price[comm] += price
            total_number[comm] += 1
    avg = {}
    for comm in total_price:
        avg[comm] = total_price[comm] / total_number[comm]
    return avg

print(average_prices((('gouda cheese 1 lbs', 3.49), ('organic oyster mushroom 1 lbs', 6.89), ('toilet paper 1 roll', 3.99), ('apple juice 1 gallon', 7.99), ('gouda cheese 1 lbs', 4.29), ('toilet paper 1 roll', 4.19), ('talenti gelato vanilla', 5.59))))




def count_bigrams(x = {}):
    some_dict = {}
    for t in range(0, len(x) - 1):
        bigram = (x[t], x[t+1])
        if bigram not in some_dict:
            some_dict[bigram] = 1
        else:
            some_dict[bigram] += 1
    return some_dict
print(count_bigrams())
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

