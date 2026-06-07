# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    word_count = dict()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def average_prices(prices):
    total_price = dict()
    total_number = dict()
    for name, price in prices:
        if name in total_price:
            total_price[name] += price
            total_number[name] += 1
        else:
            total_price[name] = price
            total_number[name] = 1
    average_price = dict()
    for name in total_price:
        average_price[name] = total_price[name] / total_number[name]
    return average_price


def count_bigrams(words):
    bigram_count = dict()
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_count:
            bigram_count[bigram] += 1
        else:
            bigram_count[bigram] = 1
    return bigram_count



#if __name__ == "__main__":
    words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
    print(count_words(words))  # {'he': 1, 'saw': 4, 'a': 2}

 
    prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2),
              ('d', 10.4), ('b', 4.3), ('b', 3.8))
    print(average_prices(prices))  # {'a': 1.1, 'c': 4.2, 'b': 4.0, 'd': 10.4}


    words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
    print(count_bigrams(words))
    # {('she', 'knows'): 3, ('knows', 'and'): 1, ('and', 'she'): 1,
    #            ('knows', 'that'): 2, ('that', 'he'): 1, ('he', 'knows'): 1, ('that', 'she'): 1}