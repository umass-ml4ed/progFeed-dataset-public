# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1       
    return word_count


def average_prices(prices):
    commodity_data = {}
    
    for commodity, price in prices:
        if commodity in commodity_data:
            commodity_data[commodity]['total'] += price
            commodity_data[commodity]['count'] += 1
        else:
            commodity_data[commodity] = {'total': price, 'count': 1}

    avg_prices = {}
    for commodity, data in commodity_data.items():
        avg_prices[commodity] = data['total'] / data['count']
        
    return avg_prices

def count_bigrams(words):
    if not isinstance(words, tuple):
        return {}
    
    if len(words) < 2:
        return {}
    
    bigram_count = {}
    
    try:
        for i in range(len(words) - 1):
            if not isinstance(words[i], str) or not isinstance(words[i + 1], str):
                continue
                
            bigram = (words[i], words[i + 1])
            bigram_count[bigram] = bigram_count.get(bigram, 0) + 1
            
    except Exception as e:
        print(f"Error in count_bigrams: {e}")
        return {}
    
    return bigram_count