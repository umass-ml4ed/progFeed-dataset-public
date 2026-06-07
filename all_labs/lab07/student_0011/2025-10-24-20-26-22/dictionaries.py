# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    some_dict = {}
    for word in words:
        some_dict[word]=words.count(word)
    return some_dict
words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))
word = ('we', 'we', 'he', 'they')
print(count_words(word))
wordss = ('school', 'class', 'learn', 'school', 'learn')
print(count_words(wordss))

def average_prices(tupleoftuples):
    some_dict={}
    for tuplee in tupleoftuples:
        name = tuplee[0]
        price = tuplee[1]
        if name not in some_dict:
            some_dict[name]=[price]
        else:
            some_dict[name].append(price)
    avgprices={}
    for key in some_dict:
        prices = some_dict[key]
        avgprices[key]=sum(prices)/len(prices)
    return avgprices
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(words):
    some_dict={}
    listt = []
    x = 0
    for n in words:
        while x+1 < len(words):
             z = words[x]
             b = words[x+1]
             zb = (z, b)
             x=x+1
             listt.append(zb)
             some_dict[zb]=listt.count(zb)
    return some_dict
   
      
wordsss = ('he', 'know', 'nd', 'se', 'know', 'at', 'he', 'know', 'hat', 'se', 'knows')
print(count_bigrams(wordsss))    

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

wors = ('he', 'he', 'she','she', 'she', 'he')
print(count_bigrams(wors))
