# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# def count_words(str):
#     some_dict = {}
#     for i in str:
#         if i not in some_dict:
#             some_dict[i] = 1
#         elif i in some_dict:
#             some_dict[i] += 1
#     return some_dict

# words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
# print(count_words(words))

def average_prices(str):
    total_price = {}
    total_count = {}
    average = {}
    for i, j in str:
        #print(f'i: {i}, j: {j}')
        if i not in total_price:
            total_price[i] = j
        else:
            total_price[i] += j
        if i not in total_count:
            total_count[i] = 1
        else:
            total_count[i] += 1

    for key in total_price:
        a = total_price[key]
        c = total_count[key]
        ave = (a / c)
        average[key] = ave
    return average
prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))
