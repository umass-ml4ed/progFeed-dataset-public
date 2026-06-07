# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def count_words(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

def average_prices(prices):
    total = {}
    count = {}
    for name, price in prices:
        total[name] = total.get(name, 0) + price
        count[name] = count.get(name, 0) + 1

    averages = {name: total[name] / count[name] for name in total}
    
    return averages

def count_bigrams(words):
    some_dict = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        some_dict[bigram] = some_dict.get(bigram, 0) + 1
    return some_dict    

print(count_bigrams(())) # returns {}
print(count_bigrams(('hello',))) # returns {}

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that',
'she', 'knows')
print(count_bigrams(words))
