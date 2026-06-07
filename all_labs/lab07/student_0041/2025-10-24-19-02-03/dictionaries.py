# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tuString):
    some_dict = {}
    for key in tuString:
        if(key in some_dict):
            some_dict[key] += 1
        else:
            some_dict[key] = 1
    return some_dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))
# Output → {'he': 1, 'saw': 4, 'a': 2}

def average_prices(commodity):
    total_number = {}
    total_price = {}
    #average = {}
    for key in commodity:
        # key ('a', 1.0)
        letter = key[0]
        price = key[1]
        if(letter in total_number):
            total_price[letter] += price
            total_number[letter] += 1 # for incrementing
        else:
            total_price[letter] = price
            total_number[letter] = 1

    average = {}
    for key in total_price:
        average[key] = total_price[key]/total_number[key]
    return average


prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))
# Output → {'a': 1.1, 'c': 4.2, 'b': 4.0, 'd': 10.4}

def count_bigrams(words):
    some_dict = {}
    for key in range(0, len(words)-1):
        bigram = (words[key], words[key+1]) # paran. to make it a tuple
        if(bigram in some_dict):
            some_dict[bigram] += 1
        else:
            some_dict[bigram] = 1
    return some_dict

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

# Output → {('she', 'knows'): 3, ('knows', 'and'): 1, ('and', 'she'): 1, ('knows', 'that'): 2, ('that', 'he'): 1, ('he', 'knows'): 1, ('that', 'she'): 1}