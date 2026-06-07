# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    word_count = {}
    for word in words:
        frequency = words.count(word)
        word_count[word] = frequency
    return word_count

def average_prices(collection):
    average_price = {}
    for item in collection:
        if item[0] not in average_price:
            average_price[item[0]] = item[1]
        else:
            average_price[item[0]] += item[1]
    for item_id in average_price:
        count = 0
        for item in collection:
            if item[0] == item_id:
                count += 1
        average_price[item_id] = average_price[item_id]/count
    return average_price

def count_bigrams(words):
    bigrams = {}
    for id in range(len(words)-1):
        if (words[id], words[id+1]) in bigrams:
            bigrams[(words[id], words[id+1])] += 1
        else:
            bigrams[(words[id], words[id+1])] = 1
    return bigrams
        
words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

#Output → {('she', 'knows'): 3, ('knows', 'and'): 1, ('and', 'she'): 1, ('knows', 'that'): 2, ('that', 'he'): 1, ('he', 'knows'): 1, ('that', 'she'): 1}
