# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words:tuple):
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count
    

words = ('apple', 'banana', 'apple', 'cherry', 'banana', 'apple')
print(count_words(words))

def average_prices(prices):
    # Dictionary to store total price and count for each commodity
    commodity_data = {}
    
    # Loop through all price entries
    for commodity, price in prices:
        if commodity in commodity_data:
            # Update existing commodity: add to total and increment count
            commodity_data[commodity]['total'] += price
            commodity_data[commodity]['count'] += 1
        else:
            # Initialize new commodity
            commodity_data[commodity] = {'total': price, 'count': 1}
    
    # Calculate averages
    averages = {}
    for commodity, data in commodity_data.items():
        averages[commodity] = data['total'] / data['count']
    
    return averages


# Alternative implementation using lists (as suggested in the hint)
def average_prices_alternative(prices):
    """
    Alternative implementation using lists to store all prices.
    """
    commodity_prices = {}
    
    # Group all prices by commodity
    for commodity, price in prices:
        if commodity in commodity_prices:
            commodity_prices[commodity].append(price)
        else:
            commodity_prices[commodity] = [price]
    
    # Calculate averages
    averages = {}
    for commodity, price_list in commodity_prices.items():
        averages[commodity] = sum(price_list) / len(price_list)
    
    return averages
    
def count_bigrams(words):
    bigram_count = {}
    
    # Loop through the words, stopping at the second-to-last word
    for i in range(len(words) - 1):
        # Create a tuple for the current bigram (current word and next word)
        bigram = (words[i], words[i + 1])
        
        # Count the bigram
        if bigram in bigram_count:
            bigram_count[bigram] += 1
        else:
            bigram_count[bigram] = 1
    
    return bigram_count
