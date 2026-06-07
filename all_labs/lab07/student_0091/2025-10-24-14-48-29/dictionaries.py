# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED




words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
def count_words(words):
    some_dict= {}
    for word in words:
        if word in some_dict:
            some_dict[word] +=1
        elif word not in some_dict:
            some_dict[word]=1
    return some_dict

print(count_words(words))


def average_prices(item_tuple)->dict:
    average_price_dict=dict()



