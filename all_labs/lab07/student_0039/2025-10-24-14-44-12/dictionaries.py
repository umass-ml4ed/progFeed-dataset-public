#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def count_words(tuple_of_words: tuple) -> dict:
    dict_to_return = {}
    for word in tuple_of_words:
        if word in dict_to_return:
            dict_to_return[word] += 1
        else:
            dict_to_return[word] = 1
    return dict_to_return

def average_prices(commodities: tuple) -> dict:
    total_price = {}
    number_of_occurences = {}
    for commodity_pair in commodities:
        if commodity_pair[0] in total_price:
            total_price[commodity_pair[0]] += commodity_pair[1]
        else:
            total_price[commodity_pair[0]] = commodity_pair[1]
        if commodity_pair[0] in number_of_occurences:
            number_of_occurences[commodity_pair[0]] += 1
        else:
            number_of_occurences[commodity_pair[0]] = 1
    for commodity in total_price:
        total_price[commodity] = total_price[commodity]/number_of_occurences[commodity]
    return total_price

def count_bigrams(words: tuple) -> dict:
    dictionary_to_return = {}
    for i in range(len(words)-1):
        if (words[i], words[i+1]) in dictionary_to_return:
            dictionary_to_return[(words[i], words[i+1])] += 1
        else:
            dictionary_to_return[(words[i], words[i+1])] = 1
    return dictionary_to_return

                                        
