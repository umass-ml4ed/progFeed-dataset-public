# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


"""count_words which takes a tuple of words as input, and returns a dictionary where the
key of each entry is a unique word from the input, and the value is the number of times that word
appears in the input. Specifically, your function should:
Take a tuple of strings as the input parameter. You may assume the strings are all lower-case.
Create an empty dictionary to begin with, for example by some_dict = {}
Loop over the input tuple. For each string in the tuple, if it doesn’t exist in the dictionary yet 
(you may use the in operator to check if a key exists in the dictionary), add it to the dictionary with a
value of 1 (i.e. first occurrence). If it already exists, increment the value by 1.
After the loop, return the dictionary."""

def count_words(words):
    word_count = {}
    for w in words:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1
    return word_count

# words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
# print(count_words(words))
# Expected output → {'he': 1, 'saw': 4, 'a': 2}


""" average_prices that takes a collection of commodities
and their prices, and returns a dictionary where the key of each entry is a unique commodity name from
the input, and the value is the average price of that commodity. The input is given as a tuple, where
each item is itself a 2-element tuple representing the name of the commodity and its price.
Take the input described above as the parameter. Assume all commodity names are lower-case.
Return a dictionary where the key of each entry is a unique commodity name (a string) from the
input, and the value is the average price of that unique commodity.
Do NOT ask the user for any input. Do NOT print anything in your function. Do NOT use nested
loops as this exercise does NOT need nested loops. (You may use other functions in the loop
however, like sum() or len())"""

def average_prices(prices):
    total = {}
    count = {}
    for item, price in prices:
        if item in total:
            total[item] += price
            count[item] += 1
        else:
            total[item] = price
            count[item] = 1
    avg = {}
    for item in total:
        avg[item] = round(total[item] / count[item], 1)
    return avg

# prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
# print(average_prices(prices))
# Expected output → {'a': 1.1, 'c': 4.2, 'b': 4.0, 'd': 10.4}


"""count
_
bigrams which takes a tuple of individual words as input, and returns a
dictionary where the key of each entry is a unique bigram from the input, and the value is the number of
times that bigram occurs. In this exercise, we will represent a bigram by a tuple of two words, for
example: ('this','is'). Specifically, your function should:
Take a tuple of strings as the input parameter. You may assume the strings are all lower-case.
Create an empty dictionary to begin with, for example by some_dict = {}
Loop over the input tuple. Each word and its following word form a bigram, which you should
represent by a tuple of the two words. If a bigram does not exist in the dictionary yet, add it to the
dictionary with a value of 1 (i.e. first occurrence). If it already exists, increment the value by 1.
After the loop, return the dictionary.
Do NOT ask the user for any input. Do NOT print anything in your function. Do NOT use nested
loops as this exercise does NOT need nested loops. Using a nested loop would mean we need to
compare/use every string in comparison to every other string, this is not needed as bigrams are
only concerned with the string directly after or before the current string."""


def count_bigrams(words):
    bigram_count = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_count:
            bigram_count[bigram] += 1
        else:
            bigram_count[bigram] = 1
    return bigram_count

# print(count_bigrams(()))            # Expected output → {}
# print(count_bigrams(('hello',)))    # Expected output → {}
# words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
# print(count_bigrams(words))
# Expected output → {
#     ('she', 'knows'): 3,
#     ('knows', 'and'): 1,
#     ('and', 'she'): 1,
#     ('knows', 'that'): 2,
#     ('that', 'he'): 1,
#     ('he', 'knows'): 1,
#     ('that', 'she'): 1
# }