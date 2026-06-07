# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_words(tuple_of_words):
    word_count = {}
    for word in tuple_of_words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1 
    return word_count

def average_prices(commodities_prices):
    commodity = {}
    price_appearance = {}
    for commodities in commodities_prices:
        if commodities[0] not in commodity:
            commodity[commodities[0]] = commodities[1]
            price_appearance[commodities[0]] = 1
        else:
            commodity[commodities[0]] += commodities[1]
            price_appearance[commodities[0]] += 1
    average = {}
    for stuff in commodity:
        average[stuff] = commodity.get(stuff)/price_appearance.get(stuff)
    return average

def count_bigrams(individual_words):
    bigram = {}
    count = 1
    if len(individual_words) < 2:
        return bigram
    for word in individual_words:
        if count < len(individual_words):
            if (word, individual_words[count]) not in bigram:
                print(word,individual_words[count])
                bigram[(word, individual_words[count])] = 1
                count += 1
            else:
                print(word,individual_words[count])
                bigram[(word, individual_words[count])] += 1
                count += 1
    return bigram


