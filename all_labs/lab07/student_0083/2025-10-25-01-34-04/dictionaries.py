# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def count_words(words_tuple):
    word_counts = {}  
    for word in words_tuple:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts



def average_prices(price_data):

    total_prices = {}
    counts = {}

    for item, price in price_data:
        if item in total_prices:
            total_prices[item] += price
            counts[item] += 1
        else:
            total_prices[item] = price
            counts[item] = 1


    avg_prices = {}
    for item in total_prices:
        avg_prices[item] = round(total_prices[item] / counts[item], 1)
    return avg_prices



def count_bigrams(words_tuple):
    bigram_counts = {}

   
    if len(words_tuple) < 2:
        return bigram_counts

    
    for i in range(len(words_tuple) - 1):
        bigram = (words_tuple[i], words_tuple[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts



if __name__ == "__main__":
    words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
    print(count_words(words))
 


    prices = (
        ('a', 1.0), ('c', 4.2), ('b', 3.9),
        ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8)
    )
    print(average_prices(prices))
 

  
    words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
    print(count_bigrams(words))
 
    print(count_bigrams(()))         
    print(count_bigrams(('hello',)))   

    


            
        