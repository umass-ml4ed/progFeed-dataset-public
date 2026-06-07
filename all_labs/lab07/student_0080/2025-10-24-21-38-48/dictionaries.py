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
    if len(words) < 2:
        return bigram_count
    

    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        
        if bigram in bigram_count:
            bigram_count[bigram] += 1
        else:
            bigram_count[bigram] = 1
            
    return bigram_count


# Tests
if __name__ == "__main__":
    print("Testing count_words:")
    words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
    print(count_words(words))
    
    print("\nTesting average_prices:")
    prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
    result = average_prices(prices)
    print(result)
    
    print("\nTesting count_bigrams:")
    print(count_bigrams(()))  
    print(count_bigrams(('hello',)))  
    words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
    result = count_bigrams(words)
    print(result)


    print("\nAdditional bigram test:")
    test_words = ('this', 'is', 'a', 'test')
    print(count_bigrams(test_words))
 