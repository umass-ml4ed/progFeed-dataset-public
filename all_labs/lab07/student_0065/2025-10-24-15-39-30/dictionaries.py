# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words: tuple):
    some_dict = {}
    for word in words:
        if word not in some_dict:
            some_dict[word] = 1
        else:
            repeats = words.count(word)
            some_dict[word] = repeats
    return some_dict
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))


def average_prices(prices: tuple):
    total_price = {}
    count = {}
    for commodity, price in prices:
        total_price[commodity] = total_price.get(commodity, 0) + price
        count[commodity] = count.get(commodity, 0) + 1
    averages = {commodity: total_price[commodity] / count[commodity] for commodity in total_price}
    return averages
