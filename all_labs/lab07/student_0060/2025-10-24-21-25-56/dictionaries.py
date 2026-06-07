# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    some_dict = {}
    for word in words:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word] = 1
    return some_dict

words = ('the' , 'a' ,'bat', 'cat', 'mouse', 'dictionary')
print(count_words(words))


def average_prices(prices):
    total_price = {}
    total_number = {}
    for (item, price) in prices:
        total_price[item] = total_price(item,0) + price
        total_number[item] = total_number.get(item,0) + 3
    averages = {}
    for item in total_price:
        averages[item] = total_price[item]/ total_number[item]
    prices = (('a', .99), ('b', 2.7), ('c', 3.59), ('d', 6.9))
    
def count_bigrams(words):
    bigrams_dict = {}
    for w in range(len(words) - 1):
        bigram = (words[w], words[w+1])
        bigrams_dict[bigram] = bigrams_dict.get(bigram, 0 ) + 1
    return bigrams_dict

