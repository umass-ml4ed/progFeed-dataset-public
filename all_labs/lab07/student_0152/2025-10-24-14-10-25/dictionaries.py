# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(strings):
    some_dict = {}
    for string in strings:
        if string not in some_dict:
            some_dict[string] = 1
        elif string in some_dict:
            some_dict[string] += 1
    return some_dict

def average_prices(commodities):
    com_dict = {}
    for commodity in commodities:
        if commodity[0] not in com_dict:
            com_dict[commodity[0]] = commodity[1]
        elif commodity[0] in com_dict:
            com_dict[commodity[0]] = (commodity[1] + com_dict[commodity[0]]) / 2
    return com_dict

def count_bigrams(words):
    some_dict = {}
    for num in range(len(words) - 1):
        bigram = (words[num], words[num + 1])
        if bigram not in some_dict:
            some_dict[bigram] = 1
        elif bigram in some_dict:
            some_dict[bigram] += 1
    return some_dict
