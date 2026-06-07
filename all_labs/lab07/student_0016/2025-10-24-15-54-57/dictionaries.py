# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words_to_count):
    word_dict = {}
    for word in words_to_count:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

# Test
words_tup = ("wow", "yes", "no", "egg", "wow", "sleepy")
print(f"Actual: {count_words(words_tup)}")
print("Expected: {'wow': 2, 'yes': 1, 'no': 1, 'egg': 1, 'sleepy': 1}")

def average_prices(prices_tup):
    item_total_prices = {}
    for item in prices_tup:
        if item[0] in item_total_prices:
            item_total_prices[item[0]].append(item[1])
        else:
            item_total_prices[item[0]] = [item[1]]
    item_average_prices = {}
    for item in item_total_prices:
        item_average_prices[item] = (sum(item_total_prices[item]) / len(item_total_prices[item]))
    return item_average_prices

def count_bigrams(phrase):
    bigram_dict = {}
    if len(phrase) < 2:
        return bigram_dict
    else:
        for i in range(len(phrase) - 1):
            bigram = (phrase[i], phrase[i + 1])
            if bigram in bigram_dict:
                bigram_dict[bigram] += 1
            else:
                bigram_dict[bigram] = 1
    return bigram_dict