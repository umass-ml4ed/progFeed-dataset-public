# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(word):
    some_dict = {}
    for words in word:
        if words in some_dict:
            some_dict[words] += 1
        else:
            some_dict[word] = 1
    return some_dict

word = ('the' , 'a' ,'bat', 'cat', 'mouse', 'dictionary')
print(count_words(word))


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
    print(average_prices(prices))

