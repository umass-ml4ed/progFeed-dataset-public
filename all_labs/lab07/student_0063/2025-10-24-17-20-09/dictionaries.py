# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


'''write a function called count_words which takes a tuple of words as input, 
and returns a dictionary where the key of each entry is a unique word from the input, 
and the value is the number of times that word appears in the input. Specifically, your function should:
Take a tuple of strings as the input parameter. You may assume the strings are all lower-case.
Create an empty dictionary to begin with, for example by some_dict = {}
Loop over the input tuple. For each string in the tuple,
if it doesn’t exist in the dictionary yet 
(you may use the in operator to check if a key exists in the dictionary), 
add it to the dictionary with a value of 1 (i.e. first occurrence). If it already exists, increment the value by 1.
After the loop, return the dictionary.
Do NOT ask the user for any input. Do NOT print anything in your function.
'''

def count_words(tup):
    d = {}
    for word in tup:
        if word not in d:
            d[word] = 1 
        else:
            d[word] += 1
    return d

'''tup = ('free', 'be', 'see', 'me', 'we', 'we', 'be')
print(count_words(tup))'''

'''write a function called average_prices that takes a collection of commodities and their prices, 
and returns a dictionary where the key of each entry is a unique commodity name from the input, 
and the value is the average price of that commodity. The input is given as a tuple, 
where each item is itself a 2-element tuple representing the name of the commodity and its price.
For example: (('gouda cheese 1 lbs', 3.49), ('organic oyster mushroom 1 lbs', 6.89), 
 ('toilet paper 1 roll', 3.99), ('apple juice 1 gallon', 7.99), ('gouda cheese 1 lbs', 4.29), 
 ('toilet paper 1 roll', 4.19), ('talenti gelato vanilla', 5.59))
As you can see, it’s a tuple of tuples: the size of the top-level tuple is the number of collected commodities, 
and each item in the top-level tuple is a 2-element tuple of the commodity name and price. Specifically, your function should:
Take the input described above as the parameter. Assume all commodity names are lower-case.
Return a dictionary where the key of each entry is a unique commodity name (a string) from the input, 
and the value is the average price of that unique commodity. 
Do NOT ask the user for any input. Do NOT print anything in your function. 
Do NOT use nested loops as this exercise does NOT need nested loops. 
(You may use other functions in the loop however, like sum() or len())

Hint: there are several ways to implement this function. For example, 
you may create two dictionaries one storing the total price, 
and the other the total number of every unique commodity seen so far as you loop over the input. 
Then in the end you use the two dictionaries to calculate the average price of each unique commodity.
Remember: If you loop over a dictionary, you are only accessing the keys, and must use those keys to access the values.
'''

def average_prices(tup):
    total = {}
    avg = {}
    item = {}
    for com in tup:
        if com[0] not in total:
            total[com[0]] = com[1]
            item[com[0]] = 1
        else:
            total[com[0]] += com[1]
            item[com[0]] += 1

    for n in total:
        avg[n] = total[n] / item[n]
    return avg

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))


'''Write a function called count_bigrams which takes a tuple of individual words as input, 
and returns a dictionary where the key of each entry is a unique bigram from the input, 
and the value is the number of times that bigram occurs. In this exercise, we will represent a bigram by a tuple of two words, 
for example: ('this', 'is'). Specifically, your function should:
Take a tuple of strings as the input parameter. You may assume the strings are all lower-case.
Create an empty dictionary to begin with, for example by some_dict = {}
Loop over the input tuple. Each word and its following word form a bigram, 
which you should represent by a tuple of the two words. If a bigram does not exist in the dictionary yet, 
add it to the dictionary with a value of 1 (i.e. first occurrence). If it already exists, increment the value by 1.
After the loop, return the dictionary.Do NOT ask the user for any input. Do NOT print anything in your function. 
Do NOT use nested loops as this exercise does NOT need nested loops. 
Using a nested loop would mean we need to compare/use every string in comparison to every other string, 
this is not needed as bigrams are only concerned with the string directly after or before the current string.'''

def count_bigrams(tup):
    d = {}
    for i in range(len(tup) - 1):
        bg = (tup[i], tup[i + 1])
        if bg not in d:
            d[bg] = 1
        else:
            d[bg] += 1

    return d

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

