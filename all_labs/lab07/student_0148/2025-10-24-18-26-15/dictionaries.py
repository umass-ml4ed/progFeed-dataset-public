 # Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    some_dict={}
    for word in words:
        if word not in some_dict:
            some_dict[word]=1
        else:
            some_dict[word]+=1
    return some_dict

def average_prices(items):
    price_dict={}
    num_dict={}
    avg_dict={}
    for item,price in items:
        if item not in price_dict:
            price_dict[item]=price
            num_dict[item]=1
        else:
            price_dict[item]+=price
            num_dict[item]+=1
    
    for item in price_dict:
        avg_dict[item]=price_dict[item]/num_dict[item]
    return avg_dict


def count_bigrams(words):
    bigram_dict={}
    for i in range(len(words)-1):
        bigram=(words[i],words[i+1])
        if bigram not in bigram_dict:
            bigram_dict[bigram]=1
        else:
            bigram_dict[bigram]+=1
    return bigram_dict

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))