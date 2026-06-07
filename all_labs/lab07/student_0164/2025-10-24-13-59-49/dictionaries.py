# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED


def count_words(words):
    some_dict = {}
    for word in words:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word] = 1
    return some_dict

words = ('umass', 'rhianna', 'seventeen', 'celery')
print(count_words(words))

def average_prices(commodities):
    total_price = {}
    total_number = {}
    
    for commodity, price in commodities:
        if commodity in total_price:
            total_price[commodity] += price
            total_number[commodity] += 1
        else:
            total_price[commodity] = price
            total_number[commodity] = 1

    avg_dict = {}
    for commodity in total_price:
        avg_dict[commodity] = total_price[commodity] / total_number[commodity]
    return avg_dict




    
    
    

    
