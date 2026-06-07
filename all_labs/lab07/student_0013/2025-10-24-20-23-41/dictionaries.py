# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
         
            word_counts[word] = 1
    
    return word_counts




def average_prices(prices):
    total_price = {}
    count = {}

    for name, price in prices:
        if name in total_price:
            total_price[name] += price
            count[name] += 1
        else:
            total_price[name] = price
            count[name] = 1

    averages = {}
    for name in total_price:
        averages[name] = total_price[name] / count[name]

    return averages


prices = (
    ('a', 1.0),
    ('c', 4.2),
    ('b', 3.9),
    ('a', 1.2),
    ('d', 10.4),
    ('b', 4.3),
    ('b', 3.8)
)



def count_bigrams()

















