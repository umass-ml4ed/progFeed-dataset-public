# def count_words(words_tuple):
#     some_dict = {}
#     for word in words_tuple:
#         if word not in some_dict:
#             some_dict[word] = 1
#         else:
#             some_dict[word] += 1
#     return some_dict

        
# words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
# print(count_words(words))

def average_prices(prices_tuple):
    total_dict = {}
    count_dict = {}
    for item, price in prices_tuple:
        if item not in total_dict:
            total_dict[item] = price
            count_dict[item] = 1
        else:
            total_dict[item] += price
            count_dict[item] += 1

    avg_dict = {}
    for item in total_dict:
        avg_dict[item] = total_dict[item] / count_dict[item]

    return avg_dict
prices = (
    ('a', 1.0), 
    ('c', 4.2), 
    ('b', 3.9), 
    ('a', 1.2), 
    ('d', 10.4), 
    ('b', 4.3), 
    ('b', 3.8)
)

print(average_prices(prices))


def count_bigrams(words_tuple):
    bigram_dict = {}
    if len(words_tuple) < 2:
        return {}
    for i in range(len(words_tuple) - 1):
        bigram = (words_tuple[i], words_tuple[i+1])
        if bigram not in bigram_dict:
            bigram_dict[bigram] = 1
        else:
            bigram_dict[bigram] += 1
    return bigram_dict

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))