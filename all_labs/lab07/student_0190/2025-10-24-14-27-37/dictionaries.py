# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_words(tpl):
    sum_dict = {}

    for item in tpl:
        if item in sum_dict:
            sum_dict[item] += 1
        else:
            sum_dict[item] = 1

    return sum_dict
        
print(count_words(('a', 'b', 'b')))


def average_prices(tpl):
    average = {}
    count = {} 
    
    print()
    
    for item, price in tpl: 
        if item in average:
            average[item] += price
            count[item] += 1
        else:
            average[item] = price
            count[item] = 1

    averages = {}
    for item in average:
        averages[item] = average[item] / count[item]
    return averages


prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))

print(average_prices(prices))

    
