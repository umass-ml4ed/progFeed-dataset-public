# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_words(tpl):
    sum_dict = {}

    for item in tpl:
        if item in sum_dict:
            sum_dict[item] += 1
        else:
            sum_dict[item] = 1

    return sum_dict
        
print(count_words(('a', 'b', 'b')))


def average_prices(tpl):
    average = {}
    count = {} 
    
    print()
    
    for item, price in tpl: 
        if item in average:
            average[item] += price
            count[item] += 1

        else:
            average[item] = price
            count[item] = 1

    averages = {}
    for item in average:
        averages[item] = average[item] / count[item]
    return averages




def count_bigrams(tpl):
    sum_dict = {}
    bigram = {}

    for i in range(len(tpl)-1):
        bigram = (tpl[i], tpl[i+1])

        if bigram in sum_dict:
            sum_dict[bigram] += 1
        else:
            sum_dict[bigram] = 1

    return sum_dict


words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

    
