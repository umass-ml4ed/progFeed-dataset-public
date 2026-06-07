# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(list):
    some_dict = {}
    for values in list:
        if values in some_dict:
            some_dict[values] += 1
        else:
            some_dict[values] = 1

    return some_dict

def average_prices(items):
  
    price_data = {}  # to store total prices and counts

    # Step 1: accumulate total price and count for each commodity
    for name, price in items:
        if name in price_data:
            price_data[name]['total'] += price
            price_data[name]['count'] += 1
        else:
            price_data[name] = {'total': price, 'count': 1}

    # Step 2: compute average for each commodity
    averages = {}
    for name, data in price_data.items():
        averages[name] = data['total'] / data['count']

    return averages

def count_bigrams(words):
    some_dict = {}

    if len(words) < 2:
        return some_dict
    
    for i in range(len(words) - 1):
        bigram = (words[i], words[i+1])
        if bigram in some_dict:
            some_dict[bigram] += 1 
        else:
            some_dict[bigram] = 1
            
    return some_dict

commodities = (
    ('gouda cheese 1 lbs', 3.49),
    ('organic oyster mushroom 1 lbs', 6.89),
    ('toilet paper 1 roll', 3.99),
    ('apple juice 1 gallon', 7.99),
    ('gouda cheese 1 lbs', 4.29),
    ('toilet paper 1 roll', 4.19),
    ('talenti gelato vanilla', 5.59)
)

print(average_prices(commodities))


