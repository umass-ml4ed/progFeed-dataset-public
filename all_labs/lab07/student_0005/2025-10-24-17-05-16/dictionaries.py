# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tup):
    some_dict = {}
    for word in tup:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word]=1
    return some_dict

def average_prices(prices):
    num_of = {}
    price = {}
    for commodity in prices:
        if commodity[0] in num_of:
            num_of[commodity[0]] += 1
            price[commodity[0]] += commodity[1]
        else:
            num_of[commodity[0]] = 1
            price[commodity[0]] = commodity[1]
    for item in price:
        if item in num_of:
            price[item] = price[item]/num_of[item]
    return price

def count_bigrams(words):
    bigram_counts = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts


# words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
# print(count_words(words))

# prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
# print(average_prices(prices))

# words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
# print(count_bigrams(words))